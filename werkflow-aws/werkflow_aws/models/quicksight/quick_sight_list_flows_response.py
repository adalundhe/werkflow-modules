from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_flow_summary import QuickSightFlowSummary


class QuickSightListFlowsResponse(BaseModel):
    FlowSummaryList: list[QuickSightFlowSummary] | None = None
    NextToken: StrictStr | None = None
    RequestId: StrictStr | None = None
    Status: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
