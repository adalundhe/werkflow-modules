from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rekognition_detect_labels_image_properties import RekognitionDetectLabelsImageProperties
from .rekognition_label import RekognitionLabel


class RekognitionDetectLabelsResponse(BaseModel):
    Labels: list[RekognitionLabel] | None = None
    OrientationCorrection: StrictStr | None = None
    LabelModelVersion: StrictStr | None = None
    ImageProperties: RekognitionDetectLabelsImageProperties | None = None
    ResponseMetadata: dict[str, Any] | None = None
