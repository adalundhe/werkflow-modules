from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .q_business_chat_output_stream import QBusinessChatOutputStream


class QBusinessChatResponse(BaseModel):
    outputStream: QBusinessChatOutputStream | None = None
    ResponseMetadata: dict[str, Any] | None = None
