from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ConnectCreateAuthCodeResponse(BaseModel):
    AuthCode: StrictStr | None = None
    SessionId: StrictStr | None = None
    EntityType: StrictStr | None = None
    EntityId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
