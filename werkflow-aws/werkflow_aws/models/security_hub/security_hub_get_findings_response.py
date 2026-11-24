from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .security_hub_aws_security_finding import SecurityHubAwsSecurityFinding


class SecurityHubGetFindingsResponse(BaseModel):
    Findings: list[SecurityHubAwsSecurityFinding] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
