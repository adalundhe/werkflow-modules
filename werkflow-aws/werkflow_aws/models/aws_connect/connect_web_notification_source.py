from __future__ import annotations
from pydantic import BaseModel
from .connect_source_campaign import ConnectSourceCampaign


class ConnectWebNotificationSource(BaseModel):
    SourceCampaign: ConnectSourceCampaign
