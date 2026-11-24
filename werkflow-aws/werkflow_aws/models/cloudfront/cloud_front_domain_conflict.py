from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontDomainConflict(BaseModel):
    Domain: StrictStr | None = None
    ResourceType: StrictStr | None = None
    ResourceId: StrictStr | None = None
    AccountId: StrictStr | None = None
