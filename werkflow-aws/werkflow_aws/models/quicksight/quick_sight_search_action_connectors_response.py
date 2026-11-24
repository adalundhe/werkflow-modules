from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_action_connector_summary import QuickSightActionConnectorSummary


class QuickSightSearchActionConnectorsResponse(BaseModel):
    NextToken: StrictStr | None = None
    RequestId: StrictStr | None = None
    Status: StrictInt | None = None
    ActionConnectorSummaries: list[QuickSightActionConnectorSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
