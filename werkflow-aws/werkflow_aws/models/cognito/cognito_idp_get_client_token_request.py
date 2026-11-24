from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPGetClientTokenRequest(BaseModel):
    ClientId: StrictStr
    Secret: StrictStr
    Scopes: list[StrictStr] | None = None
    ClientMetadata: dict[StrictStr, StrictStr] | None = None
