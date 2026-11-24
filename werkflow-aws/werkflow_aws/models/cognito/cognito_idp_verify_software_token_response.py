from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class CognitoIDPVerifySoftwareTokenResponse(BaseModel):
    Status: StrictStr | None = None
    Session: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
