from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessDeleteConversationRequest(BaseModel):
    conversationId: StrictStr
    applicationId: StrictStr
    userId: StrictStr | None = None
