from __future__ import annotations
from pydantic import BaseModel
from .security_hub_aws_security_finding import SecurityHubAwsSecurityFinding


class SecurityHubBatchImportFindingsRequest(BaseModel):
    Findings: list[SecurityHubAwsSecurityFinding]
