from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .document_db_event import DocumentDBEvent


class DocumentDBDescribeEventsResponse(BaseModel):
    Marker: StrictStr | None = None
    Events: list[DocumentDBEvent] | None = None
    ResponseMetadata: dict[str, Any] | None = None
