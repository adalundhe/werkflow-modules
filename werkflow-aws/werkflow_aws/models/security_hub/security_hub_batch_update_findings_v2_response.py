from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .security_hub_batch_update_findings_v2_processed_finding import SecurityHubBatchUpdateFindingsV2ProcessedFinding
from .security_hub_batch_update_findings_v2_unprocessed_finding import SecurityHubBatchUpdateFindingsV2UnprocessedFinding


class SecurityHubBatchUpdateFindingsV2Response(BaseModel):
    ProcessedFindings: list[SecurityHubBatchUpdateFindingsV2ProcessedFinding] | None = None
    UnprocessedFindings: list[SecurityHubBatchUpdateFindingsV2UnprocessedFinding] | None = None
    ResponseMetadata: dict[str, Any] | None = None
