from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .document_db_filter import DocumentDBFilter


class DocumentDBDescribeEventCategoriesRequest(BaseModel):
    SourceType: StrictStr | None = None
    Filters: list[DocumentDBFilter] | None = None
