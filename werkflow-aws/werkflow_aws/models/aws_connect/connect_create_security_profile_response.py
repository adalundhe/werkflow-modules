from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ConnectCreateSecurityProfileResponse(BaseModel):
    SecurityProfileId: StrictStr | None = None
    SecurityProfileArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
