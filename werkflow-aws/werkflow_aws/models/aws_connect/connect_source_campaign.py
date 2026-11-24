from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectSourceCampaign(BaseModel):
    CampaignId: StrictStr | None = None
    OutboundRequestId: StrictStr | None = None
