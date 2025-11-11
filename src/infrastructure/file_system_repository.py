import json
import os
from typing import List
from src.domain.diagram import Diagram

class FileSystemDiagramRepository:
    def __init__(self, flowchart_path="flowchart", mindmap_path="mindmap", timeline_path="timeline"):
        self.paths = {
            "flowchart": flowchart_path,
            "mindmap": mindmap_path,
            "timeline": timeline_path
        }

    def get_all(self) -> List[Diagram]:
        diagrams = []
        for diagram_type, base_path in self.paths.items():
            diagrams.extend(self._get_diagrams_from_path(base_path, diagram_type))
        return diagrams

    def get_by_id(self, diagram_id: str, diagram_type: str = None) -> Diagram:
        if diagram_type == "flowchart":
            return self._get_by_id_from_path(diagram_id, self.paths["flowchart"])
        elif diagram_type == "mindmap":
            return self._get_by_id_from_path(diagram_id, self.paths["mindmap"])
        elif diagram_type == "timeline":
            return self._get_by_id_from_path(diagram_id, self.paths["timeline"])
        
        for path in ("flowchart", "mindmap", "timeline"):
            result = self._get_by_id_from_path(diagram_id, self.paths[path])
            if result:
                return result
        return None
    
    def _get_by_id_from_path(self, diagram_id: str, base_path: str) -> Diagram:
        if not os.path.exists(base_path):
            return None
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

    def _get_diagrams_from_path(self, base_path: str, diagram_type: str) -> List[Diagram]:
        diagrams = []
        if not os.path.exists(base_path):
            return diagrams
        for root, _, files in os.walk(base_path):
            if "jsons" in root:
                area = os.path.basename(os.path.dirname(root))
                json_files = [f for f in files if f.endswith(".json") and not f.endswith(".bak")]
                json_files.sort(key=lambda f: int(f.split("_")[0]) if f.split("_")[0].isdigit() else float("inf"))
                for file in json_files:
                    filepath = os.path.join(root, file)
                    number = int(file.split("_")[0])
                    with open(filepath, "r", encoding="utf-8") as f:
                        data = json.load(f)
                        for diagram_data in data.get("diagrams", []):
                            diagram_data["area"] = area
                            diagram_data["number"] = number
                            if "diagram_type" not in diagram_data:
                                diagram_data["diagram_type"] = diagram_type
                            diagrams.append(Diagram(**diagram_data))
        return diagrams
