from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .quick_sight_agent import QuickSightAgent


class QuickSightDescribeAgentResponse(BaseModel):
    Agent: QuickSightAgent | None = None
    RequestId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
