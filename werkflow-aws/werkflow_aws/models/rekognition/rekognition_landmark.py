from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class RekognitionLandmark(BaseModel):
    Type: StrictStr | None = None
    X: StrictFloat | StrictInt | None = None
    Y: StrictFloat | StrictInt | None = None
