from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .q_business_chat_response_configuration_detail import QBusinessChatResponseConfigurationDetail


class QBusinessGetChatResponseConfigurationResponse(BaseModel):
    chatResponseConfigurationId: StrictStr | None = None
    chatResponseConfigurationArn: StrictStr | None = None
    displayName: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    inUseConfiguration: QBusinessChatResponseConfigurationDetail | None = None
    lastUpdateConfiguration: QBusinessChatResponseConfigurationDetail | None = None
    ResponseMetadata: dict[str, Any] | None = None
