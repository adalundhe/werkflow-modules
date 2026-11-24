from __future__ import annotations
from pydantic import BaseModel
from .textract_event_bridge_configuration import TextractEventBridgeConfiguration


class TextractNotificationConfiguration(BaseModel):
    EventBridgeConfiguration: TextractEventBridgeConfiguration
