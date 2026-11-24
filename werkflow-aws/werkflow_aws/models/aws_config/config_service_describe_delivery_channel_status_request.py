from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceDescribeDeliveryChannelStatusRequest(BaseModel):
    DeliveryChannelNames: list[StrictStr] | None = None
