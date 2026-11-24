from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointCampaignState(BaseModel):
    CampaignStatus: StrictStr | None = None
