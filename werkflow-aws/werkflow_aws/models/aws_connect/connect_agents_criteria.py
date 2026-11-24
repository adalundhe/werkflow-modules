from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectAgentsCriteria(BaseModel):
    AgentIds: list[StrictStr] | None = None
