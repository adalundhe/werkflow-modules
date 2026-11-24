from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPTokenValidityUnitsType(BaseModel):
    AccessToken: StrictStr | None = None
    IdToken: StrictStr | None = None
    RefreshToken: StrictStr | None = None
