from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .security_hub_remediation_v2_item import SecurityHubRemediationV2Item


class SecurityHubGetRemediationsV2Response(BaseModel):
    Items: list[SecurityHubRemediationV2Item] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
