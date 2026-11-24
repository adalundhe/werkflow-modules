from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectAgentHierarchyGroups(BaseModel):
    L1Ids: list[StrictStr] | None = None
    L2Ids: list[StrictStr] | None = None
    L3Ids: list[StrictStr] | None = None
    L4Ids: list[StrictStr] | None = None
    L5Ids: list[StrictStr] | None = None
