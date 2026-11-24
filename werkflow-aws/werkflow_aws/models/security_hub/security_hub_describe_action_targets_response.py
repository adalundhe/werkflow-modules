from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .security_hub_action_target import SecurityHubActionTarget


class SecurityHubDescribeActionTargetsResponse(BaseModel):
    ActionTargets: list[SecurityHubActionTarget] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
