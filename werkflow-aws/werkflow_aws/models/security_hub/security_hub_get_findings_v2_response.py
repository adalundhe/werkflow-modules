from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .security_hub_ocsf_finding import SecurityHubOcsfFinding


class SecurityHubGetFindingsV2Response(BaseModel):
    Findings: list[SecurityHubOcsfFinding] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
