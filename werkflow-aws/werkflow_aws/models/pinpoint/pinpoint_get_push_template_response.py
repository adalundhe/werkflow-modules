from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_push_notification_template_response import PinpointPushNotificationTemplateResponse


class PinpointGetPushTemplateResponse(BaseModel):
    PushNotificationTemplateResponse: PinpointPushNotificationTemplateResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
