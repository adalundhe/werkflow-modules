from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessGetChatResponseConfigurationRequest(BaseModel):
    applicationId: StrictStr
    chatResponseConfigurationId: StrictStr
