from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPVerifySoftwareTokenRequest(BaseModel):
    UserCode: StrictStr
    AccessToken: StrictStr | None = None
    Session: StrictStr | None = None
    FriendlyDeviceName: StrictStr | None = None
