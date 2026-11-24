from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .rekognition_custom_label import RekognitionCustomLabel


class RekognitionDetectCustomLabelsResponse(BaseModel):
    CustomLabels: list[RekognitionCustomLabel] | None = None
    ResponseMetadata: dict[str, Any] | None = None
