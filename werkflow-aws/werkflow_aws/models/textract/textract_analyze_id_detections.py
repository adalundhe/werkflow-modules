from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .textract_normalized_value import TextractNormalizedValue


class TextractAnalyzeIDDetections(BaseModel):
    Text: StrictStr | None = None
    NormalizedValue: TextractNormalizedValue | None = None
    Confidence: StrictFloat | StrictInt | None = None
