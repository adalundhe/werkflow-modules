from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointCampaignCustomMessage(BaseModel):
    Data: StrictStr | None = None
