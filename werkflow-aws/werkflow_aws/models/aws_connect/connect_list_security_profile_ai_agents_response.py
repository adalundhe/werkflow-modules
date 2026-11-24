from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_ai_agent import ConnectAIAgent


class ConnectListSecurityProfileAIAgentsResponse(BaseModel):
    AllowedAIAgents: list[ConnectAIAgent] | None = None
    NextToken: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedRegion: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
