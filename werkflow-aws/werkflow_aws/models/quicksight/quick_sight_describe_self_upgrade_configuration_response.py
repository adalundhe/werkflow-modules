from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_self_upgrade_configuration import QuickSightSelfUpgradeConfiguration


class QuickSightDescribeSelfUpgradeConfigurationResponse(BaseModel):
    SelfUpgradeConfiguration: QuickSightSelfUpgradeConfiguration | None = None
    RequestId: StrictStr | None = None
    Status: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
