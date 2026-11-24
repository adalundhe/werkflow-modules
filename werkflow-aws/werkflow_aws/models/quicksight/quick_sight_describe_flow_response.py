from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_flow_detail import QuickSightFlowDetail


class QuickSightDescribeFlowResponse(BaseModel):
    Flow: QuickSightFlowDetail | None = None
    RequestId: StrictStr | None = None
    Status: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
