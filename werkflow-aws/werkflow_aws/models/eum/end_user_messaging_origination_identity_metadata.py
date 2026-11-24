from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EndUserMessagingOriginationIdentityMetadata(BaseModel):
    OriginationIdentityArn: StrictStr | None = None
    OriginationIdentity: StrictStr | None = None
    IsoCountryCode: StrictStr | None = None
    NumberCapabilities: list[StrictStr] | None = None
    PhoneNumber: StrictStr | None = None
