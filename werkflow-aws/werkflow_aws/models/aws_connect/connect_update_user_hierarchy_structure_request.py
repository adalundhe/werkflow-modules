from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_hierarchy_structure_update import ConnectHierarchyStructureUpdate


class ConnectUpdateUserHierarchyStructureRequest(BaseModel):
    HierarchyStructure: ConnectHierarchyStructureUpdate
    InstanceId: StrictStr
