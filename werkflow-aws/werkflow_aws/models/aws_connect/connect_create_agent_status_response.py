from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ConnectCreateAgentStatusResponse(BaseModel):
    AgentStatusARN: StrictStr | None = None
    AgentStatusId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
