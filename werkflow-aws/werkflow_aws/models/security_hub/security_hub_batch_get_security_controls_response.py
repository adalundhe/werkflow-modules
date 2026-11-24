from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .security_hub_security_control import SecurityHubSecurityControl
from .security_hub_unprocessed_security_control import SecurityHubUnprocessedSecurityControl


class SecurityHubBatchGetSecurityControlsResponse(BaseModel):
    SecurityControls: list[SecurityHubSecurityControl] | None = None
    UnprocessedIds: list[SecurityHubUnprocessedSecurityControl] | None = None
    ResponseMetadata: dict[str, Any] | None = None
