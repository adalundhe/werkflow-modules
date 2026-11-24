from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .simplified_hierarchy_level import SimplifiedHierarchyLevel


class Hierarchy(BaseModel):
    baseLevelId: StrictInt | None = None
    levels: list[SimplifiedHierarchyLevel] | None = None
