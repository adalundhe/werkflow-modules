from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class EndUserMessagingPutMessageFeedbackResponse(BaseModel):
    MessageId: StrictStr | None = None
    MessageFeedbackStatus: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
