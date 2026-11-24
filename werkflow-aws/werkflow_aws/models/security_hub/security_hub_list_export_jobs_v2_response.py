from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .security_hub_export_summary import SecurityHubExportSummary


class SecurityHubListExportJobsV2Response(BaseModel):
    Items: list[SecurityHubExportSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
