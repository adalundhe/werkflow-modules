from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr


class EndUserMessagingSetDefaultMessageFeedbackEnabledResponse(BaseModel):
    ConfigurationSetArn: StrictStr | None = None
    ConfigurationSetName: StrictStr | None = None
    MessageFeedbackEnabled: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
