from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .security_hub_standards_control import SecurityHubStandardsControl


class SecurityHubDescribeStandardsControlsResponse(BaseModel):
    Controls: list[SecurityHubStandardsControl] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
