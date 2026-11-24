from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt
from .security_hub_import_findings_error import SecurityHubImportFindingsError


class SecurityHubBatchImportFindingsResponse(BaseModel):
    FailedCount: StrictInt | None = None
    SuccessCount: StrictInt | None = None
    FailedFindings: list[SecurityHubImportFindingsError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
