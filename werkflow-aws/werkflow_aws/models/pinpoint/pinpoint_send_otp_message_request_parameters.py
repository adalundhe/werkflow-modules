from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class PinpointSendOTPMessageRequestParameters(BaseModel):
    BrandName: StrictStr
    Channel: StrictStr
    DestinationIdentity: StrictStr
    OriginationIdentity: StrictStr
    ReferenceId: StrictStr
    AllowedAttempts: StrictInt | None = None
    CodeLength: StrictInt | None = None
    EntityId: StrictStr | None = None
    Language: StrictStr | None = None
    TemplateId: StrictStr | None = None
    ValidityPeriod: StrictInt | None = None
