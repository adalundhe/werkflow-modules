from __future__ import annotations
from pydantic import BaseModel
from .connect_hierarchy_group_summary import ConnectHierarchyGroupSummary


class ConnectHierarchyPath(BaseModel):
    LevelOne: ConnectHierarchyGroupSummary | None = None
    LevelTwo: ConnectHierarchyGroupSummary | None = None
    LevelThree: ConnectHierarchyGroupSummary | None = None
    LevelFour: ConnectHierarchyGroupSummary | None = None
    LevelFive: ConnectHierarchyGroupSummary | None = None
