from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointDefaultPushNotificationTemplate(BaseModel):
    Action: StrictStr | None = None
    Body: StrictStr | None = None
    Sound: StrictStr | None = None
    Title: StrictStr | None = None
    Url: StrictStr | None = None
