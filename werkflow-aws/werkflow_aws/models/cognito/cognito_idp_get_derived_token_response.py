from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class CognitoIDPGetDerivedTokenResponse(BaseModel):
    IssuedToken: StrictStr | None = None
    IssuedTokenType: StrictStr | None = None
    TokenType: StrictStr | None = None
    ExpiresIn: StrictInt | None = None
    Scopes: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
