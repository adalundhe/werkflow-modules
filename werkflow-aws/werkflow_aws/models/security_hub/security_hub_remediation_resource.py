from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubRemediationResource(BaseModel):
    AccountId: StrictStr | None = None
    Region: StrictStr | None = None
    ResourceOwnerAccountId: StrictStr | None = None
    ResourceOwnerOrgId: StrictStr | None = None
    Type: StrictStr | None = None
    Name: StrictStr | None = None
    Id: StrictStr | None = None
    ResourceGuid: StrictStr | None = None
    ResourceRegion: StrictStr | None = None
    CloudProvider: StrictStr | None = None
