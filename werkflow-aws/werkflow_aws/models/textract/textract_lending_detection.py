from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .textract_geometry import TextractGeometry


class TextractLendingDetection(BaseModel):
    Text: StrictStr | None = None
    SelectionStatus: StrictStr | None = None
    Geometry: TextractGeometry | None = None
    Confidence: StrictFloat | StrictInt | None = None
