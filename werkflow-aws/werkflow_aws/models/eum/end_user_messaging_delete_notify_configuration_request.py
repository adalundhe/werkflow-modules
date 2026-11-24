from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EndUserMessagingDeleteNotifyConfigurationRequest(BaseModel):
    NotifyConfigurationId: StrictStr
