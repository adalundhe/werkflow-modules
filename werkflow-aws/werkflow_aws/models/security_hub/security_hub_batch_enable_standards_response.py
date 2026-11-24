from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .security_hub_standards_subscription import SecurityHubStandardsSubscription


class SecurityHubBatchEnableStandardsResponse(BaseModel):
    StandardsSubscriptions: list[SecurityHubStandardsSubscription] | None = None
    ResponseMetadata: dict[str, Any] | None = None
