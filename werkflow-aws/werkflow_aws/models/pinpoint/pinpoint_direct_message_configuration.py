from __future__ import annotations
from pydantic import BaseModel
from .pinpoint_adm_message import PinpointADMMessage
from .pinpoint_apns_message import PinpointAPNSMessage
from .pinpoint_baidu_message import PinpointBaiduMessage
from .pinpoint_default_message import PinpointDefaultMessage
from .pinpoint_default_push_notification_message import PinpointDefaultPushNotificationMessage
from .pinpoint_email_message import PinpointEmailMessage
from .pinpoint_gcm_message import PinpointGCMMessage
from .pinpoint_sms_message import PinpointSMSMessage
from .pinpoint_voice_message import PinpointVoiceMessage


class PinpointDirectMessageConfiguration(BaseModel):
    ADMMessage: PinpointADMMessage | None = None
    APNSMessage: PinpointAPNSMessage | None = None
    BaiduMessage: PinpointBaiduMessage | None = None
    DefaultMessage: PinpointDefaultMessage | None = None
    DefaultPushNotificationMessage: PinpointDefaultPushNotificationMessage | None = None
    EmailMessage: PinpointEmailMessage | None = None
    GCMMessage: PinpointGCMMessage | None = None
    SMSMessage: PinpointSMSMessage | None = None
    VoiceMessage: PinpointVoiceMessage | None = None
