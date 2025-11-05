from typing import List, Dict
from src.application.services import DiagramService
from src.domain.diagram import Diagram

class ListDiagramsUseCase:
    def __init__(self, diagram_service: DiagramService):
        self.diagram_service = diagram_service

    def execute(self) -> Dict[str, List[Diagram]]:
        diagrams = self.diagram_service.get_all_diagrams()
        diagrams_sorted = sorted(diagrams, key=lambda d: d.number)
        
        grouped_diagrams = {}
        for diagram in diagrams_sorted:
            if diagram.area not in grouped_diagrams:
                grouped_diagrams[diagram.area] = []
            grouped_diagrams[diagram.area].append(diagram)

        return grouped_diagrams

class GetDiagramUseCase:
    def __init__(self, diagram_service: DiagramService):
        self.diagram_service = diagram_service

    def execute(self, diagram_id: str) -> Diagram:
        return self.diagram_service.get_diagram_by_id(diagram_id)
