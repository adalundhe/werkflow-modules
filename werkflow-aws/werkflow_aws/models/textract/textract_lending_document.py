from __future__ import annotations
from pydantic import BaseModel
from .textract_lending_field import TextractLendingField
from .textract_signature_detection import TextractSignatureDetection


class TextractLendingDocument(BaseModel):
    LendingFields: list[TextractLendingField] | None = None
    SignatureDetections: list[TextractSignatureDetection] | None = None
