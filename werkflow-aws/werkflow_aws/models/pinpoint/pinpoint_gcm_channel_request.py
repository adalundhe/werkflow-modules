from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class PinpointGCMChannelRequest(BaseModel):
    ApiKey: StrictStr | None = None
    DefaultAuthenticationMethod: StrictStr | None = None
    Enabled: StrictBool | None = None
    ServiceJson: StrictStr | None = None
