from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .document_db_event_categories_map import DocumentDBEventCategoriesMap


class DocumentDBDescribeEventCategoriesResponse(BaseModel):
    EventCategoriesMapList: list[DocumentDBEventCategoriesMap] | None = None
    ResponseMetadata: dict[str, Any] | None = None
