from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .textract_geometry import TextractGeometry


class TextractExpenseDetection(BaseModel):
    Text: StrictStr | None = None
    Geometry: TextractGeometry | None = None
    Confidence: StrictFloat | StrictInt | None = None
