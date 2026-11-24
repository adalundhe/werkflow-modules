from __future__ import annotations
from pydantic import BaseModel
from .security_hub_findings_output import SecurityHubFindingsOutput


class SecurityHubExportOutput(BaseModel):
    Findings: SecurityHubFindingsOutput | None = None
