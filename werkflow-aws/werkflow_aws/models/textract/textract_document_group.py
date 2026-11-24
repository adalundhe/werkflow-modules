from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .textract_detected_signature import TextractDetectedSignature
from .textract_split_document import TextractSplitDocument
from .textract_undetected_signature import TextractUndetectedSignature


class TextractDocumentGroup(BaseModel):
    Type: StrictStr | None = None
    SplitDocuments: list[TextractSplitDocument] | None = None
    DetectedSignatures: list[TextractDetectedSignature] | None = None
    UndetectedSignatures: list[TextractUndetectedSignature] | None = None
