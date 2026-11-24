from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class RekognitionTechnicalCueSegment(BaseModel):
    Type: StrictStr | None = None
    Confidence: StrictFloat | StrictInt | None = None
