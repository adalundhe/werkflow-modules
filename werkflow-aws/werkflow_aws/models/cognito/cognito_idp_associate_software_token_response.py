from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class CognitoIDPAssociateSoftwareTokenResponse(BaseModel):
    SecretCode: StrictStr | None = None
    Session: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
