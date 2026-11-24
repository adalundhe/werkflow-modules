from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceDeliverConfigSnapshotRequest(BaseModel):
    deliveryChannelName: StrictStr
