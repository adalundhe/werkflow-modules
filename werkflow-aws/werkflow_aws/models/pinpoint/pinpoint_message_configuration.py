from __future__ import annotations
from pydantic import BaseModel
from .pinpoint_campaign_custom_message import PinpointCampaignCustomMessage
from .pinpoint_campaign_email_message import PinpointCampaignEmailMessage
from .pinpoint_campaign_in_app_message import PinpointCampaignInAppMessage
from .pinpoint_campaign_sms_message import PinpointCampaignSmsMessage
from .pinpoint_message import PinpointMessage


class PinpointMessageConfiguration(BaseModel):
    ADMMessage: PinpointMessage | None = None
    APNSMessage: PinpointMessage | None = None
    BaiduMessage: PinpointMessage | None = None
    CustomMessage: PinpointCampaignCustomMessage | None = None
    DefaultMessage: PinpointMessage | None = None
    EmailMessage: PinpointCampaignEmailMessage | None = None
    GCMMessage: PinpointMessage | None = None
    SMSMessage: PinpointCampaignSmsMessage | None = None
    InAppMessage: PinpointCampaignInAppMessage | None = None
