from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .polly_recording_data import PollyRecordingData


class PollyRecording(BaseModel):
    Format: StrictStr | None = None
    Data: PollyRecordingData | None = None
