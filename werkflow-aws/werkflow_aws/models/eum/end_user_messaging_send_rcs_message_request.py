from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .end_user_messaging_rcs_fallback_configuration import EndUserMessagingRcsFallbackConfiguration
from .end_user_messaging_rcs_message_content import EndUserMessagingRcsMessageContent


class EndUserMessagingSendRcsMessageRequest(BaseModel):
    DestinationPhoneNumber: StrictStr
    OriginationIdentity: StrictStr
    RcsMessageContent: EndUserMessagingRcsMessageContent | None = None
    TimeToLive: StrictInt | None = None
    MessageTrafficType: StrictStr | None = None
    FallbackConfiguration: EndUserMessagingRcsFallbackConfiguration | None = None
    ProtectConfigurationId: StrictStr | None = None
    ConfigurationSetName: StrictStr | None = None
    MaxPrice: StrictStr | None = None
    DryRun: StrictBool | None = None
    Context: dict[StrictStr, StrictStr] | None = None
    MessageFeedbackEnabled: StrictBool | None = None
