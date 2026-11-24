from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .pinpoint_push_notification_template_request import PinpointPushNotificationTemplateRequest


class PinpointUpdatePushTemplateRequest(BaseModel):
    PushNotificationTemplateRequest: PinpointPushNotificationTemplateRequest
    TemplateName: StrictStr
    CreateNewVersion: StrictBool | None = None
    Version: StrictStr | None = None
