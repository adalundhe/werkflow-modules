from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_push_notification_template_request import PinpointPushNotificationTemplateRequest


class PinpointCreatePushTemplateRequest(BaseModel):
    PushNotificationTemplateRequest: PinpointPushNotificationTemplateRequest
    TemplateName: StrictStr
