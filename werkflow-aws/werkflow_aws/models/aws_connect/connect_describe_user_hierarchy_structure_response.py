from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .connect_hierarchy_structure import ConnectHierarchyStructure


class ConnectDescribeUserHierarchyStructureResponse(BaseModel):
    HierarchyStructure: ConnectHierarchyStructure | None = None
    ResponseMetadata: dict[str, Any] | None = None
