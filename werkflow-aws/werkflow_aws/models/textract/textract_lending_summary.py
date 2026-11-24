from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .textract_document_group import TextractDocumentGroup


class TextractLendingSummary(BaseModel):
    DocumentGroups: list[TextractDocumentGroup] | None = None
    UndetectedDocumentTypes: list[StrictStr] | None = None
