from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SupportAddAttachmentsToSetResponse(BaseModel):
    attachmentSetId: StrictStr | None = None
    expiryTime: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
