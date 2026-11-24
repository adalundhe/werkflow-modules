from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_ai_agent_info import ConnectAiAgentInfo


class ConnectWisdomInfo(BaseModel):
    SessionArn: StrictStr | None = None
    AiAgents: list[ConnectAiAgentInfo] | None = None
