from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EndUserMessagingSendMediaMessageRequest(BaseModel):
    DestinationPhoneNumber: StrictStr
    OriginationIdentity: StrictStr
    MessageBody: StrictStr | None = None
    MediaUrls: list[StrictStr] | None = None
    ConfigurationSetName: StrictStr | None = None
    MaxPrice: StrictStr | None = None
    TimeToLive: StrictInt | None = None
    Context: dict[StrictStr, StrictStr] | None = None
    DryRun: StrictBool | None = None
    ProtectConfigurationId: StrictStr | None = None
    MessageFeedbackEnabled: StrictBool | None = None
