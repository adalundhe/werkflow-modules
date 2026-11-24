from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .security_hub_resource_severity_breakdown import SecurityHubResourceSeverityBreakdown


class SecurityHubResourceFindingsSummary(BaseModel):
    FindingType: StrictStr | None = None
    ProductName: StrictStr | None = None
    TotalFindings: StrictInt | None = None
    Severities: SecurityHubResourceSeverityBreakdown | None = None
