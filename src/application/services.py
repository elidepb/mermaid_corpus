import json
from typing import List
from src.domain.diagram import Diagram

class DiagramService:
    def __init__(self, repository, error_cache_path="src/diagram_errors.json"):
        self.repository = repository
        self.error_cache = self._load_error_cache(error_cache_path)

    def _load_error_cache(self, path: str) -> dict:
        try:
            with open(path, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def get_all_diagrams(self) -> List[Diagram]:
        diagrams = self.repository.get_all()
        for diagram in diagrams:
            diagram.has_errors = self.error_cache.get(diagram.id, False)
        return diagrams

    def get_diagram_by_id(self, diagram_id: str, diagram_type: str = None) -> Diagram:
        diagram = self.repository.get_by_id(diagram_id, diagram_type)
        if diagram:
            diagram.has_errors = self.error_cache.get(diagram.id, False)
        return diagram
