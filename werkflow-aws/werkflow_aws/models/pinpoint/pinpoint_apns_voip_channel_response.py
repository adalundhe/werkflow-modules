from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class PinpointAPNSVoipChannelResponse(BaseModel):
    ApplicationId: StrictStr | None = None
    CreationDate: StrictStr | None = None
    DefaultAuthenticationMethod: StrictStr | None = None
    Enabled: StrictBool | None = None
    HasCredential: StrictBool | None = None
    HasTokenKey: StrictBool | None = None
    Id: StrictStr | None = None
    IsArchived: StrictBool | None = None
    LastModifiedBy: StrictStr | None = None
    LastModifiedDate: StrictStr | None = None
    Platform: StrictStr | None = None
    Version: StrictInt | None = None
