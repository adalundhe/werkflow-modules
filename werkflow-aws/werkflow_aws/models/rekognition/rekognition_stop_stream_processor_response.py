from __future__ import annotations
from typing import Any
from pydantic import BaseModel


class RekognitionStopStreamProcessorResponse(BaseModel):
    ResponseMetadata: dict[str, Any] | None = None
