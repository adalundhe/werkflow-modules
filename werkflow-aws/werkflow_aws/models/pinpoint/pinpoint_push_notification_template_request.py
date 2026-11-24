from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_apns_push_notification_template import PinpointAPNSPushNotificationTemplate
from .pinpoint_android_push_notification_template import PinpointAndroidPushNotificationTemplate
from .pinpoint_default_push_notification_template import PinpointDefaultPushNotificationTemplate


class PinpointPushNotificationTemplateRequest(BaseModel):
    ADM: PinpointAndroidPushNotificationTemplate | None = None
    APNS: PinpointAPNSPushNotificationTemplate | None = None
    Baidu: PinpointAndroidPushNotificationTemplate | None = None
    Default: PinpointDefaultPushNotificationTemplate | None = None
    DefaultSubstitutions: StrictStr | None = None
    GCM: PinpointAndroidPushNotificationTemplate | None = None
    RecommenderId: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    TemplateDescription: StrictStr | None = None
