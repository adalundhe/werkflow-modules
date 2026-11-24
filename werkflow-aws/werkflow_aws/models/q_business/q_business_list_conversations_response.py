from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .q_business_conversation import QBusinessConversation


class QBusinessListConversationsResponse(BaseModel):
    nextToken: StrictStr | None = None
    conversations: list[QBusinessConversation] | None = None
    ResponseMetadata: dict[str, Any] | None = None
