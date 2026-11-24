from __future__ import annotations
from pydantic import BaseModel
from .q_business_conversation_source import QBusinessConversationSource


class QBusinessCopyFromSource(BaseModel):
    conversation: QBusinessConversationSource | None = None
