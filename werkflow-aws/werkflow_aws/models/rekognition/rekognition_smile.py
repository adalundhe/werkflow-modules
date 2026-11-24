from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt


class RekognitionSmile(BaseModel):
    Value: StrictBool | None = None
    Confidence: StrictFloat | StrictInt | None = None
