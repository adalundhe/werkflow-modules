from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .config_service_delivery_channel_status import ConfigServiceDeliveryChannelStatus


class ConfigServiceDescribeDeliveryChannelStatusResponse(BaseModel):
    DeliveryChannelsStatus: list[ConfigServiceDeliveryChannelStatus] | None = None
    ResponseMetadata: dict[str, Any] | None = None
