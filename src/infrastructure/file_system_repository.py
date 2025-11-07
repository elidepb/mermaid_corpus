import json
import os
from typing import List
from src.domain.diagram import Diagram

class FileSystemDiagramRepository:
    def __init__(self, flowchart_path="flowchart", mindmap_path="mindmap"):
        self.flowchart_path = flowchart_path
        self.mindmap_path = mindmap_path

    def get_all(self) -> List[Diagram]:
        diagrams = []
        
        # Load flowcharts
        if os.path.exists(self.flowchart_path):
            for root, _, files in os.walk(self.flowchart_path):
                if "jsons" in root:
                    area = os.path.basename(os.path.dirname(root))
                    # Sort files by numeric prefix to ensure proper order
                    json_files = [f for f in files if f.endswith(".json") and not f.endswith(".bak")]
                    json_files.sort(key=lambda f: int(f.split("_")[0]) if f.split("_")[0].isdigit() else float('inf'))
                    for file in json_files:
                        filepath = os.path.join(root, file)
                        number = int(file.split("_")[0])
                        with open(filepath, "r", encoding="utf-8") as f:
                            data = json.load(f)
                            for diagram_data in data.get("diagrams", []):
                                diagram_data["area"] = area
                                diagram_data["number"] = number
                                diagrams.append(Diagram(**diagram_data))
        
        # Load mindmaps (now with same structure as flowcharts)
        if os.path.exists(self.mindmap_path):
            for root, _, files in os.walk(self.mindmap_path):
                if "jsons" in root:
                    area = os.path.basename(os.path.dirname(root))
                    # Sort files by numeric prefix to ensure proper order
                    json_files = [f for f in files if f.endswith(".json") and not f.endswith(".bak")]
                    json_files.sort(key=lambda f: int(f.split("_")[0]) if f.split("_")[0].isdigit() else float('inf'))
                    for file in json_files:
                        filepath = os.path.join(root, file)
                        number = int(file.split("_")[0])
                        with open(filepath, "r", encoding="utf-8") as f:
                            data = json.load(f)
                            for diagram_data in data.get("diagrams", []):
                                diagram_data["area"] = area
                                diagram_data["number"] = number
                                diagrams.append(Diagram(**diagram_data))
        
        return diagrams

    def get_by_id(self, diagram_id: str, diagram_type: str = None) -> Diagram:
        # If diagram_type is specified, search only in that type
        if diagram_type == "flowchart":
            return self._get_by_id_from_path(diagram_id, self.flowchart_path)
        elif diagram_type == "mindmap":
            return self._get_by_id_from_path(diagram_id, self.mindmap_path)
        
        # If no type specified, search in flowcharts first (backward compatibility)
        if os.path.exists(self.flowchart_path):
            result = self._get_by_id_from_path(diagram_id, self.flowchart_path)
            if result:
                return result
        
        # Then search in mindmaps
        if os.path.exists(self.mindmap_path):
            return self._get_by_id_from_path(diagram_id, self.mindmap_path)
        
        return None
    
    def _get_by_id_from_path(self, diagram_id: str, base_path: str) -> Diagram:
        """Helper method to search for a diagram by ID in a specific path"""
        for root, _, files in os.walk(base_path):
            if "jsons" in root:
                area = os.path.basename(os.path.dirname(root))
                for file in files:
                    if file.endswith(".json") and not file.endswith(".bak"):
                        filepath = os.path.join(root, file)
                        number = int(file.split("_")[0])
                        with open(filepath, "r", encoding="utf-8") as f:
                            data = json.load(f)
                            for diagram_data in data.get("diagrams", []):
                                if diagram_data["id"] == diagram_id:
                                    diagram_data["area"] = area
                                    diagram_data["number"] = number
                                    return Diagram(**diagram_data)
        return None
