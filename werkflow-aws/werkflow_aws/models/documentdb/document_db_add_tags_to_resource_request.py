from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .document_db_tag import DocumentDBTag


class DocumentDBAddTagsToResourceRequest(BaseModel):
    ResourceName: StrictStr
    Tags: list[DocumentDBTag]
