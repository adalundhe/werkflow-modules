from __future__ import annotations
from pydantic import BaseModel
from .security_hub_findings_output_summary import SecurityHubFindingsOutputSummary


class SecurityHubExportOutputSummary(BaseModel):
    Findings: SecurityHubFindingsOutputSummary | None = None
