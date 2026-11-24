from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EndUserMessagingSendVoiceMessageRequest(BaseModel):
    DestinationPhoneNumber: StrictStr
    OriginationIdentity: StrictStr
    MessageBody: StrictStr | None = None
    MessageBodyTextType: Literal['TEXT', 'SSML'] | None = None
    VoiceId: StrictStr | None = None
    ConfigurationSetName: StrictStr | None = None
    MaxPricePerMinute: StrictStr | None = None
    TimeToLive: StrictInt | None = None
    Context: dict[StrictStr, StrictStr] | None = None
    DryRun: StrictBool | None = None
    ProtectConfigurationId: StrictStr | None = None
    MessageFeedbackEnabled: StrictBool | None = None
