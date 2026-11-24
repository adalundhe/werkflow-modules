from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EndUserMessagingRegistrationAssociationMetadata(BaseModel):
    ResourceArn: StrictStr | None = None
    ResourceId: StrictStr | None = None
    ResourceType: StrictStr | None = None
    IsoCountryCode: StrictStr | None = None
    PhoneNumber: StrictStr | None = None
