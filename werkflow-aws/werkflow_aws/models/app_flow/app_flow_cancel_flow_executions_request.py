from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppFlowCancelFlowExecutionsRequest(BaseModel):
    flowName: StrictStr
    executionIds: list[StrictStr] | None = None
