from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class RedshiftModifyAuthenticationProfileResponse(BaseModel):
    AuthenticationProfileName: StrictStr | None = None
    AuthenticationProfileContent: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
