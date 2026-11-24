from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SecurityHubEnableSecurityHubV2Response(BaseModel):
    HubV2Arn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
