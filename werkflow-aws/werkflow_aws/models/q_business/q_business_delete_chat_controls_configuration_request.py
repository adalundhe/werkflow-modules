from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessDeleteChatControlsConfigurationRequest(BaseModel):
    applicationId: StrictStr
