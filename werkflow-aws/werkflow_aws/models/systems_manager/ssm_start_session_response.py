from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SSMStartSessionResponse(BaseModel):
    SessionId: StrictStr | None = None
    TokenValue: StrictStr | None = None
    StreamUrl: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
