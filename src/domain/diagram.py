from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Diagram:
    id: str
    topic: str
    category: str
    description: str
    diagram_type: str
    mermaid_code: str
    complexity: str
    tags: List[str]
    creation_date: str
    area: str
    number: int
    has_errors: Optional[bool] = None
