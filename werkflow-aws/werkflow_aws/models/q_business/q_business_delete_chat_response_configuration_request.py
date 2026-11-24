from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessDeleteChatResponseConfigurationRequest(BaseModel):
    applicationId: StrictStr
    chatResponseConfigurationId: StrictStr
