from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .security_hub_aws_security_finding_identifier import SecurityHubAwsSecurityFindingIdentifier
from .security_hub_batch_update_findings_unprocessed_finding import SecurityHubBatchUpdateFindingsUnprocessedFinding


class SecurityHubBatchUpdateFindingsResponse(BaseModel):
    ProcessedFindings: list[SecurityHubAwsSecurityFindingIdentifier] | None = None
    UnprocessedFindings: list[SecurityHubBatchUpdateFindingsUnprocessedFinding] | None = None
    ResponseMetadata: dict[str, Any] | None = None
