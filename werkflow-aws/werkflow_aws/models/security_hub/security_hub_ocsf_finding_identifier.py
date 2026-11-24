from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubOcsfFindingIdentifier(BaseModel):
    CloudAccountUid: StrictStr | None = None
    FindingInfoUid: StrictStr | None = None
    MetadataProductUid: StrictStr | None = None
