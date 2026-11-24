from __future__ import annotations
from pydantic import BaseModel
from .connect_hierarchy_group_summary_reference import ConnectHierarchyGroupSummaryReference


class ConnectHierarchyPathReference(BaseModel):
    LevelOne: ConnectHierarchyGroupSummaryReference | None = None
    LevelTwo: ConnectHierarchyGroupSummaryReference | None = None
    LevelThree: ConnectHierarchyGroupSummaryReference | None = None
    LevelFour: ConnectHierarchyGroupSummaryReference | None = None
    LevelFive: ConnectHierarchyGroupSummaryReference | None = None
