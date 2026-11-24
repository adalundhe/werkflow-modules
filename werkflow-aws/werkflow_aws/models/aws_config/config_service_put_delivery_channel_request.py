from __future__ import annotations
from pydantic import BaseModel
from .config_service_delivery_channel import ConfigServiceDeliveryChannel


class ConfigServicePutDeliveryChannelRequest(BaseModel):
    DeliveryChannel: ConfigServiceDeliveryChannel
