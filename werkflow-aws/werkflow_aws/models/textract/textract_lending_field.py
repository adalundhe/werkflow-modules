from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .textract_lending_detection import TextractLendingDetection


class TextractLendingField(BaseModel):
    Type: StrictStr | None = None
    KeyDetection: TextractLendingDetection | None = None
    ValueDetections: list[TextractLendingDetection] | None = None
