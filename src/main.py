from fastapi import FastAPI, Request
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
async def read_root(request: Request):
    diagrams = list_diagrams_use_case.execute()
    return templates.TemplateResponse(request, "index.html", {"diagrams": diagrams})

@app.get("/diagrams/{diagram_id}", response_class=HTMLResponse)
async def read_diagram(request: Request, diagram_id: str):
    diagram = get_diagram_use_case.execute(diagram_id)
    return templates.TemplateResponse(request, "diagram.html", {"diagram": diagram})
