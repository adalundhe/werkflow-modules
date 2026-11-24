from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .textract_extraction import TextractExtraction
from .textract_page_classification import TextractPageClassification


class TextractLendingResult(BaseModel):
    Page: StrictInt | None = None
    PageClassification: TextractPageClassification | None = None
    Extractions: list[TextractExtraction] | None = None
