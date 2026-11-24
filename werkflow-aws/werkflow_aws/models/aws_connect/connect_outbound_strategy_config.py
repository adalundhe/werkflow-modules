from __future__ import annotations
from pydantic import BaseModel
from .connect_agent_first import ConnectAgentFirst


class ConnectOutboundStrategyConfig(BaseModel):
    AgentFirst: ConnectAgentFirst | None = None
