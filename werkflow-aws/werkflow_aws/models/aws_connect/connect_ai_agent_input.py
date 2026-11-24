from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectAiAgentInput(BaseModel):
    AiAgentId: StrictStr
