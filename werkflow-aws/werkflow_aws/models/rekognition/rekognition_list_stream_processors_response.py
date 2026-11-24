from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rekognition_stream_processor import RekognitionStreamProcessor


class RekognitionListStreamProcessorsResponse(BaseModel):
    NextToken: StrictStr | None = None
    StreamProcessors: list[RekognitionStreamProcessor] | None = None
    ResponseMetadata: dict[str, Any] | None = None
