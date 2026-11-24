from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class RekognitionEmotion(BaseModel):
    Type: StrictStr | None = None
    Confidence: StrictFloat | StrictInt | None = None
