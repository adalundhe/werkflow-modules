from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessConversationSource(BaseModel):
    conversationId: StrictStr | None = None
    attachmentId: StrictStr | None = None
