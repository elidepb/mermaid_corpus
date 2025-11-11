from fastapi import FastAPI, Request, Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from src.application.services import DiagramService
from src.application.use_cases import GetDiagramUseCase, ListDiagramsUseCase
from src.infrastructure.file_system_repository import FileSystemDiagramRepository

app = FastAPI()

app.mount("/static", StaticFiles(directory="src/presentation/static"), name="static")
templates = Jinja2Templates(directory="src/presentation/templates")

diagram_repository = FileSystemDiagramRepository()
diagram_service = DiagramService(diagram_repository)
list_diagrams_use_case = ListDiagramsUseCase(diagram_service)
get_diagram_use_case = GetDiagramUseCase(diagram_service)

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request, tab: str = Query(default="flowchart")):
    raw_diagrams = list_diagrams_use_case.execute()
    tabs_order = ["flowchart", "mindmap", "timeline"]
    diagrams = {}
    for tab_key in tabs_order:
        diagrams[tab_key] = raw_diagrams.get(tab_key, {})
    for tab_key, value in raw_diagrams.items():
        if tab_key not in diagrams:
            diagrams[tab_key] = value
    tab_labels = {
        "flowchart": "Flowchart",
        "mindmap": "Mindmap",
        "timeline": "Timeline"
    }
    selected_tab = tab if tab in diagrams else None
    if not selected_tab:
        for tab_key in tabs_order:
            if diagrams.get(tab_key):
                selected_tab = tab_key
                break
    if not selected_tab:
        selected_tab = tabs_order[0]
    empty_messages = {
        "flowchart": "No hay diagramas de flujo disponibles.",
        "mindmap": "No hay mapas mentales disponibles.",
        "timeline": "No hay timelines disponibles."
    }
    context = {
        "diagrams": diagrams,
        "tab_labels": tab_labels,
        "tabs_order": list(diagrams.keys()),
        "selected_tab": selected_tab,
        "empty_messages": empty_messages
    }
    return templates.TemplateResponse(request, "index.html", context)

@app.get("/diagrams/{diagram_type}/{diagram_id}", response_class=HTMLResponse)
async def read_diagram(request: Request, diagram_type: str, diagram_id: str):
    diagram = get_diagram_use_case.execute(diagram_id, diagram_type)
    selected_tab = request.query_params.get("tab") or getattr(diagram, "diagram_type", diagram_type)
    context = {
        "diagram": diagram,
        "selected_tab": selected_tab
    }
    return templates.TemplateResponse(request, "diagram.html", context)
