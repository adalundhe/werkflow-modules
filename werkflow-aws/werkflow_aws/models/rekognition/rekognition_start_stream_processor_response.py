from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class RekognitionStartStreamProcessorResponse(BaseModel):
    SessionId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
