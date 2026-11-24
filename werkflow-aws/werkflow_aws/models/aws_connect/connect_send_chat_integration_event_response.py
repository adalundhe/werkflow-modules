from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr


class ConnectSendChatIntegrationEventResponse(BaseModel):
    InitialContactId: StrictStr | None = None
    NewChatCreated: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
