from __future__ import annotations
from pydantic import BaseModel
from .connect_hierarchy_level_update import ConnectHierarchyLevelUpdate


class ConnectHierarchyStructureUpdate(BaseModel):
    LevelOne: ConnectHierarchyLevelUpdate | None = None
    LevelTwo: ConnectHierarchyLevelUpdate | None = None
    LevelThree: ConnectHierarchyLevelUpdate | None = None
    LevelFour: ConnectHierarchyLevelUpdate | None = None
    LevelFive: ConnectHierarchyLevelUpdate | None = None
