from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class PinpointDefaultPushNotificationMessage(BaseModel):
    Action: Literal['OPEN_APP', 'DEEP_LINK', 'URL'] | None = None
    Body: StrictStr | None = None
    Data: dict[StrictStr, StrictStr] | None = None
    SilentPush: StrictBool | None = None
    Substitutions: dict[StrictStr, list[StrictStr]] | None = None
    Title: StrictStr | None = None
    Url: StrictStr | None = None
