from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .q_business_chat_response_configuration import QBusinessChatResponseConfiguration


class QBusinessListChatResponseConfigurationsResponse(BaseModel):
    chatResponseConfigurations: list[QBusinessChatResponseConfiguration] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
