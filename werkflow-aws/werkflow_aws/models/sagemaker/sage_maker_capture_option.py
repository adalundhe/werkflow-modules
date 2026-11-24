from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_capture_mode import SageMakerCaptureMode


class SageMakerCaptureOption(BaseModel):
    CaptureMode: SageMakerCaptureMode | None = None
