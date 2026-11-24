from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class FMSGetNotificationChannelResponse(BaseModel):
    SnsTopicArn: StrictStr | None = None
    SnsRoleName: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
