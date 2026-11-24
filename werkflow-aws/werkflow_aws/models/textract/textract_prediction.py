from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class TextractPrediction(BaseModel):
    Value: StrictStr | None = None
    Confidence: StrictFloat | StrictInt | None = None
