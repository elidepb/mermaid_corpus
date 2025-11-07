from typing import List, Dict
from src.application.services import DiagramService
from src.domain.diagram import Diagram

class ListDiagramsUseCase:
    def __init__(self, diagram_service: DiagramService):
        self.diagram_service = diagram_service

    def execute(self) -> Dict[str, Dict[str, List[Diagram]]]:
        diagrams = self.diagram_service.get_all_diagrams()
        diagrams_sorted = sorted(diagrams, key=lambda d: d.number)
        
        flowcharts_by_area = {}
        mindmaps_by_area = {}
        
        for diagram in diagrams_sorted:
            if diagram.diagram_type == "flowchart":
                if diagram.area not in flowcharts_by_area:
                    flowcharts_by_area[diagram.area] = []
                flowcharts_by_area[diagram.area].append(diagram)
            elif diagram.diagram_type == "mindmap":
                # Group mindmaps by area, same as flowcharts
                if diagram.area not in mindmaps_by_area:
                    mindmaps_by_area[diagram.area] = []
                mindmaps_by_area[diagram.area].append(diagram)
        
        # Ensure diagrams within each area are sorted by number
        for area in flowcharts_by_area:
            flowcharts_by_area[area].sort(key=lambda d: d.number)
        for area in mindmaps_by_area:
            mindmaps_by_area[area].sort(key=lambda d: d.number)

        return {
            "flowchart": flowcharts_by_area,
            "mindmap": mindmaps_by_area
        }

class GetDiagramUseCase:
    def __init__(self, diagram_service: DiagramService):
        self.diagram_service = diagram_service

    def execute(self, diagram_id: str) -> Diagram:
        return self.diagram_service.get_diagram_by_id(diagram_id)
