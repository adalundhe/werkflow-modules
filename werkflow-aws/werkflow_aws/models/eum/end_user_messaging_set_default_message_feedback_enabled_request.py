from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EndUserMessagingSetDefaultMessageFeedbackEnabledRequest(BaseModel):
    ConfigurationSetName: StrictStr
    MessageFeedbackEnabled: StrictBool
