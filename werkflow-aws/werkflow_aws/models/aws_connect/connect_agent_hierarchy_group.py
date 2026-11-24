from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectAgentHierarchyGroup(BaseModel):
    Arn: StrictStr | None = None
