from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_ocsf_finding_identifier import SecurityHubOcsfFindingIdentifier


class SecurityHubBatchUpdateFindingsV2ProcessedFinding(BaseModel):
    FindingIdentifier: SecurityHubOcsfFindingIdentifier | None = None
    MetadataUid: StrictStr | None = None
