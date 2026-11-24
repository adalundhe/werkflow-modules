from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt


class RekognitionCoversBodyPart(BaseModel):
    Confidence: StrictFloat | StrictInt | None = None
    Value: StrictBool | None = None
