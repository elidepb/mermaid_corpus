from typing import List, Dict
from src.application.services import DiagramService
from src.domain.diagram import Diagram

class ListDiagramsUseCase:
    def __init__(self, diagram_service: DiagramService):
        self.diagram_service = diagram_service

    def execute(self) -> Dict[str, Dict[str, List[Diagram]]]:
        diagrams = self.diagram_service.get_all_diagrams()
        diagrams_sorted = sorted(diagrams, key=lambda d: d.number)
        grouped: Dict[str, Dict[str, List[Diagram]]] = {}
        for diagram in diagrams_sorted:
            diagram_type = diagram.diagram_type
            if diagram_type not in grouped:
                grouped[diagram_type] = {}
            if diagram.area not in grouped[diagram_type]:
                grouped[diagram_type][diagram.area] = []
            grouped[diagram_type][diagram.area].append(diagram)
        for diagram_type in grouped:
            for area in grouped[diagram_type]:
                grouped[diagram_type][area].sort(key=lambda d: d.number)
        ordered_types = ["flowchart", "mindmap", "timeline"]
        result = {}
        for diagram_type in ordered_types:
            if diagram_type in grouped:
                result[diagram_type] = grouped[diagram_type]
        for diagram_type in grouped:
            if diagram_type not in result:
                result[diagram_type] = grouped[diagram_type]
        return result

class GetDiagramUseCase:
    def __init__(self, diagram_service: DiagramService):
        self.diagram_service = diagram_service

    def execute(self, diagram_id: str, diagram_type: str = None) -> Diagram:
        return self.diagram_service.get_diagram_by_id(diagram_id, diagram_type)
