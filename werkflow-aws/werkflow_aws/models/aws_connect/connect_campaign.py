from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectCampaign(BaseModel):
    CampaignId: StrictStr | None = None
