from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointAndroidPushNotificationTemplate(BaseModel):
    Action: StrictStr | None = None
    Body: StrictStr | None = None
    ImageIconUrl: StrictStr | None = None
    ImageUrl: StrictStr | None = None
    RawContent: StrictStr | None = None
    SmallImageIconUrl: StrictStr | None = None
    Sound: StrictStr | None = None
    Title: StrictStr | None = None
    Url: StrictStr | None = None
