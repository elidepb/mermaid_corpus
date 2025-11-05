import json
import os
from typing import List
from src.domain.diagram import Diagram

class FileSystemDiagramRepository:
    def __init__(self, data_path="flowchart"):
        self.data_path = data_path

    def get_all(self) -> List[Diagram]:
        diagrams = []
        for root, _, files in os.walk(self.data_path):
            if "jsons" in root:
                area = os.path.basename(os.path.dirname(root))
                for file in files:
                    if file.endswith(".json"):
                        filepath = os.path.join(root, file)
                        number = int(file.split("_")[0])
                        with open(filepath, "r") as f:
                            data = json.load(f)
                            for diagram_data in data.get("diagrams", []):
                                diagram_data["area"] = area
                                diagram_data["number"] = number
                                diagrams.append(Diagram(**diagram_data))
        return diagrams

    def get_by_id(self, diagram_id: str) -> Diagram:
        for root, _, files in os.walk(self.data_path):
            if "jsons" in root:
                area = os.path.basename(os.path.dirname(root))
                for file in files:
                    if file.endswith(".json"):
                        filepath = os.path.join(root, file)
                        number = int(file.split("_")[0])
                        with open(filepath, "r") as f:
                            data = json.load(f)
                            for diagram_data in data.get("diagrams", []):
                                if diagram_data["id"] == diagram_id:
                                    diagram_data["area"] = area
                                    diagram_data["number"] = number
                                    return Diagram(**diagram_data)
        return None
