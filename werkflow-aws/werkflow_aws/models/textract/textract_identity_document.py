from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .textract_block import TextractBlock
from .textract_identity_document_field import TextractIdentityDocumentField


class TextractIdentityDocument(BaseModel):
    DocumentIndex: StrictInt | None = None
    IdentityDocumentFields: list[TextractIdentityDocumentField] | None = None
    Blocks: list[TextractBlock] | None = None
