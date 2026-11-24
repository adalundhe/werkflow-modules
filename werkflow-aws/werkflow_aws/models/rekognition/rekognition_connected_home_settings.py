from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class RekognitionConnectedHomeSettings(BaseModel):
    Labels: list[StrictStr] | None = None
    MinConfidence: StrictFloat | StrictInt | None = None
