from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceDeleteDeliveryChannelRequest(BaseModel):
    DeliveryChannelName: StrictStr
