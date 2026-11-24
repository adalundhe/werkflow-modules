from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class RekognitionContentType(BaseModel):
    Confidence: StrictFloat | StrictInt | None = None
    Name: StrictStr | None = None
