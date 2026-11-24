from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .config_service_delivery_channel import ConfigServiceDeliveryChannel


class ConfigServiceDescribeDeliveryChannelsResponse(BaseModel):
    DeliveryChannels: list[ConfigServiceDeliveryChannel] | None = None
    ResponseMetadata: dict[str, Any] | None = None
