from __future__ import annotations
from pydantic import BaseModel
from .connect_agent_hierarchy_group import ConnectAgentHierarchyGroup


class ConnectHierarchyGroups(BaseModel):
    Level1: ConnectAgentHierarchyGroup | None = None
    Level2: ConnectAgentHierarchyGroup | None = None
    Level3: ConnectAgentHierarchyGroup | None = None
    Level4: ConnectAgentHierarchyGroup | None = None
    Level5: ConnectAgentHierarchyGroup | None = None
