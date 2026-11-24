from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .document_db_filter import DocumentDBFilter


class DocumentDBListTagsForResourceRequest(BaseModel):
    ResourceName: StrictStr
    Filters: list[DocumentDBFilter] | None = None
