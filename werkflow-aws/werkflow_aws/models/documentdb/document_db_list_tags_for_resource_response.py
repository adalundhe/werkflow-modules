from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .document_db_tag import DocumentDBTag


class DocumentDBListTagsForResourceResponse(BaseModel):
    TagList: list[DocumentDBTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
