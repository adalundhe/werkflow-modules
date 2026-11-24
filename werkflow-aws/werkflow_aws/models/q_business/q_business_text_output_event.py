from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessTextOutputEvent(BaseModel):
    systemMessageType: StrictStr | None = None
    conversationId: StrictStr | None = None
    userMessageId: StrictStr | None = None
    systemMessageId: StrictStr | None = None
    systemMessage: StrictStr | None = None
