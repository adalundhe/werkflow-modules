from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_action_connector import QuickSightActionConnector


class QuickSightDescribeActionConnectorResponse(BaseModel):
    ActionConnector: QuickSightActionConnector | None = None
    RequestId: StrictStr | None = None
    Status: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
