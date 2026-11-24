from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class PinpointAPNSMessage(BaseModel):
    APNSPushType: StrictStr | None = None
    Action: Literal['OPEN_APP', 'DEEP_LINK', 'URL'] | None = None
    Badge: StrictInt | None = None
    Body: StrictStr | None = None
    Category: StrictStr | None = None
    CollapseId: StrictStr | None = None
    Data: dict[StrictStr, StrictStr] | None = None
    MediaUrl: StrictStr | None = None
    PreferredAuthenticationMethod: StrictStr | None = None
    Priority: StrictStr | None = None
    RawContent: StrictStr | None = None
    SilentPush: StrictBool | None = None
    Sound: StrictStr | None = None
    Substitutions: dict[StrictStr, list[StrictStr]] | None = None
    ThreadId: StrictStr | None = None
    TimeToLive: StrictInt | None = None
    Title: StrictStr | None = None
    Url: StrictStr | None = None
