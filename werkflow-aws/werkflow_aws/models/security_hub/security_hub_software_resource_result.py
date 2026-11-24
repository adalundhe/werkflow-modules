from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubSoftwareResourceResult(BaseModel):
    AccountId: StrictStr | None = None
    ResourceType: StrictStr | None = None
    Region: StrictStr | None = None
    ResourceId: StrictStr | None = None
    ResourceProvider: StrictStr | None = None
    ResourceOwnerOrgId: StrictStr | None = None
    ResourceOwnerAccountId: StrictStr | None = None
    ResourceCloudPartition: StrictStr | None = None
    ResourceRegion: StrictStr | None = None
