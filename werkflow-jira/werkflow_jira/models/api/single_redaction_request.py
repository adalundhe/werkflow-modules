from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .content_item import ContentItem
from .redaction_position import RedactionPosition


class SingleRedactionRequest(BaseModel):
    contentItem: ContentItem | None = None
    externalId: StrictStr | None = None
    reason: StrictStr | None = None
    redactionPosition: RedactionPosition | None = None
