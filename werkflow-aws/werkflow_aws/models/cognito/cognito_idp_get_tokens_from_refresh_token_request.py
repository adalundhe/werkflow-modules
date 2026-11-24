from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPGetTokensFromRefreshTokenRequest(BaseModel):
    RefreshToken: StrictStr
    ClientId: StrictStr
    ClientSecret: StrictStr | None = None
    DeviceKey: StrictStr | None = None
    ClientMetadata: dict[StrictStr, StrictStr] | None = None
