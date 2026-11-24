from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EndUserMessagingSendNotifyTextMessageRequest(BaseModel):
    NotifyConfigurationId: StrictStr
    DestinationPhoneNumber: StrictStr
    TemplateVariables: dict[StrictStr, StrictStr]
    TemplateId: StrictStr | None = None
    TimeToLive: StrictInt | None = None
    Context: dict[StrictStr, StrictStr] | None = None
    ConfigurationSetName: StrictStr | None = None
    DryRun: StrictBool | None = None
    MessageFeedbackEnabled: StrictBool | None = None
