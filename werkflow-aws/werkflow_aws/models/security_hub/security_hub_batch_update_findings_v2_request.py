from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .security_hub_ocsf_finding_identifier import SecurityHubOcsfFindingIdentifier


class SecurityHubBatchUpdateFindingsV2Request(BaseModel):
    MetadataUids: list[StrictStr] | None = None
    FindingIdentifiers: list[SecurityHubOcsfFindingIdentifier] | None = None
    Comment: StrictStr | None = None
    SeverityId: StrictInt | None = None
    StatusId: StrictInt | None = None
