from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class QBusinessCreateChatResponseConfigurationResponse(BaseModel):
    chatResponseConfigurationId: StrictStr | None = None
    chatResponseConfigurationArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
