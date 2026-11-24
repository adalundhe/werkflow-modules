from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .q_business_message import QBusinessMessage


class QBusinessListMessagesResponse(BaseModel):
    messages: list[QBusinessMessage] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
