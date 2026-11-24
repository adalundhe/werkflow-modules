from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SageMakerStartSessionResponse(BaseModel):
    SessionId: StrictStr | None = None
    StreamUrl: StrictStr | None = None
    TokenValue: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
