from __future__ import annotations
from pydantic import BaseModel
from .connect_hierarchy_level import ConnectHierarchyLevel


class ConnectHierarchyStructure(BaseModel):
    LevelOne: ConnectHierarchyLevel | None = None
    LevelTwo: ConnectHierarchyLevel | None = None
    LevelThree: ConnectHierarchyLevel | None = None
    LevelFour: ConnectHierarchyLevel | None = None
    LevelFive: ConnectHierarchyLevel | None = None
