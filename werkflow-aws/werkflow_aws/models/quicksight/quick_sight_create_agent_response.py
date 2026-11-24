from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class QuickSightCreateAgentResponse(BaseModel):
    Arn: StrictStr | None = None
    AgentId: StrictStr | None = None
    AgentStatus: StrictStr | None = None
    AgentName: StrictStr | None = None
    RequestId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
