from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SNSPublishResponse(BaseModel):
    MessageId: StrictStr | None = None
    SequenceNumber: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
