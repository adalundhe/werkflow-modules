from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class RekognitionStartCelebrityRecognitionResponse(BaseModel):
    JobId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
