from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .q_business_attachment import QBusinessAttachment


class QBusinessListAttachmentsResponse(BaseModel):
    attachments: list[QBusinessAttachment] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
