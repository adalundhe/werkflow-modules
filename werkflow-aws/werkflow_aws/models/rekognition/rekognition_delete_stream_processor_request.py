from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RekognitionDeleteStreamProcessorRequest(BaseModel):
    Name: StrictStr
