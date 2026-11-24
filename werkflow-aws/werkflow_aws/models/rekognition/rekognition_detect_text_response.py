from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rekognition_text_detection import RekognitionTextDetection


class RekognitionDetectTextResponse(BaseModel):
    TextDetections: list[RekognitionTextDetection] | None = None
    TextModelVersion: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
