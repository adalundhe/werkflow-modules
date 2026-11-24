from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class PinpointMessage(BaseModel):
    Action: StrictStr | None = None
    Body: StrictStr | None = None
    ImageIconUrl: StrictStr | None = None
    ImageSmallIconUrl: StrictStr | None = None
    ImageUrl: StrictStr | None = None
    JsonBody: StrictStr | None = None
    MediaUrl: StrictStr | None = None
    RawContent: StrictStr | None = None
    SilentPush: StrictBool | None = None
    TimeToLive: StrictInt | None = None
    Title: StrictStr | None = None
    Url: StrictStr | None = None
