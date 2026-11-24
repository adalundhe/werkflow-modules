from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceDescribeDeliveryChannelsRequest(BaseModel):
    DeliveryChannelNames: list[StrictStr] | None = None
