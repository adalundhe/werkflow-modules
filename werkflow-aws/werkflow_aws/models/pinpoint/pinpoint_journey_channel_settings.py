from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointJourneyChannelSettings(BaseModel):
    ConnectCampaignArn: StrictStr | None = None
    ConnectCampaignExecutionRoleArn: StrictStr | None = None
