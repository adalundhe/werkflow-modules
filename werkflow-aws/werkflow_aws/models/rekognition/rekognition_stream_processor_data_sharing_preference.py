from __future__ import annotations
from pydantic import BaseModel, StrictBool


class RekognitionStreamProcessorDataSharingPreference(BaseModel):
    OptIn: StrictBool | None = None
