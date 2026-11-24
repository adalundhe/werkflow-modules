from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_self_upgrade_request_detail import QuickSightSelfUpgradeRequestDetail


class QuickSightListSelfUpgradesResponse(BaseModel):
    SelfUpgradeRequestDetails: list[QuickSightSelfUpgradeRequestDetail] | None = None
    NextToken: StrictStr | None = None
    RequestId: StrictStr | None = None
    Status: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
