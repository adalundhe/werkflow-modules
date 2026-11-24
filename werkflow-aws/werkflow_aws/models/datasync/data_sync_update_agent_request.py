from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataSyncUpdateAgentRequest(BaseModel):
    AgentArn: StrictStr
    Name: StrictStr | None = None
