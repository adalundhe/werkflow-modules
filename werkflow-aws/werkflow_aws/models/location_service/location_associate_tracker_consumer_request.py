from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LocationAssociateTrackerConsumerRequest(BaseModel):
    TrackerName: StrictStr
    ConsumerArn: StrictStr
