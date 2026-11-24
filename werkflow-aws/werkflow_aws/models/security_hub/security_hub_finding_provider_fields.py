from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .security_hub_finding_provider_severity import SecurityHubFindingProviderSeverity
from .security_hub_related_finding import SecurityHubRelatedFinding


class SecurityHubFindingProviderFields(BaseModel):
    Confidence: StrictInt | None = None
    Criticality: StrictInt | None = None
    RelatedFindings: list[SecurityHubRelatedFinding] | None = None
    Severity: SecurityHubFindingProviderSeverity | None = None
    Types: list[StrictStr] | None = None
