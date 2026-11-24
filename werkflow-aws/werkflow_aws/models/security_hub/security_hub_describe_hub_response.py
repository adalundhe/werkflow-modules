from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr


class SecurityHubDescribeHubResponse(BaseModel):
    HubArn: StrictStr | None = None
    SubscribedAt: StrictStr | None = None
    AutoEnableControls: StrictBool | None = None
    ControlFindingGenerator: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
