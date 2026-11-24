from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_security_finding_identifier import SecurityHubAwsSecurityFindingIdentifier


class SecurityHubBatchUpdateFindingsUnprocessedFinding(BaseModel):
    FindingIdentifier: SecurityHubAwsSecurityFindingIdentifier | None = None
    ErrorCode: StrictStr | None = None
    ErrorMessage: StrictStr | None = None
