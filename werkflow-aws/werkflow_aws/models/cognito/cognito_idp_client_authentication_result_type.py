from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CognitoIDPClientAuthenticationResultType(BaseModel):
    AccessToken: StrictStr | None = None
    ExpiresIn: StrictInt | None = None
    TokenType: StrictStr | None = None
