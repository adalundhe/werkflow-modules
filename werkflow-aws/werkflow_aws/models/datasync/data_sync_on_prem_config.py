from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataSyncOnPremConfig(BaseModel):
    AgentArns: list[StrictStr] | None = None
