from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_action_connector_summary import QuickSightActionConnectorSummary


class QuickSightListActionConnectorsResponse(BaseModel):
    ActionConnectorSummaries: list[QuickSightActionConnectorSummary] | None = None
    NextToken: StrictStr | None = None
    RequestId: StrictStr | None = None
    Status: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
