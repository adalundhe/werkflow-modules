from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class PinpointAPNSVoipSandboxChannelRequest(BaseModel):
    BundleId: StrictStr | None = None
    Certificate: StrictStr | None = None
    DefaultAuthenticationMethod: StrictStr | None = None
    Enabled: StrictBool | None = None
    PrivateKey: StrictStr | None = None
    TeamId: StrictStr | None = None
    TokenKey: StrictStr | None = None
    TokenKeyId: StrictStr | None = None
