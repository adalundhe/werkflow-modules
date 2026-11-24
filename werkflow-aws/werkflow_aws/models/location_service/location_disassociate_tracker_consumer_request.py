from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LocationDisassociateTrackerConsumerRequest(BaseModel):
    TrackerName: StrictStr
    ConsumerArn: StrictStr
