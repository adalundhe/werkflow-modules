from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .q_business_chat_input_stream import QBusinessChatInputStream


class QBusinessChatRequest(BaseModel):
    applicationId: StrictStr
    userId: StrictStr | None = None
    userGroups: list[StrictStr] | None = None
    conversationId: StrictStr | None = None
    parentMessageId: StrictStr | None = None
    clientToken: StrictStr | None = None
    inputStream: QBusinessChatInputStream | None = None
