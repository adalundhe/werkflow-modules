from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class RedshiftCreateAuthenticationProfileResponse(BaseModel):
    AuthenticationProfileName: StrictStr | None = None
    AuthenticationProfileContent: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
