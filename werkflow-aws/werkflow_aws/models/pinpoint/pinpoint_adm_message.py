from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class PinpointADMMessage(BaseModel):
    Action: Literal['OPEN_APP', 'DEEP_LINK', 'URL'] | None = None
    Body: StrictStr | None = None
    ConsolidationKey: StrictStr | None = None
    Data: dict[StrictStr, StrictStr] | None = None
    ExpiresAfter: StrictStr | None = None
    IconReference: StrictStr | None = None
    ImageIconUrl: StrictStr | None = None
    ImageUrl: StrictStr | None = None
    MD5: StrictStr | None = None
    RawContent: StrictStr | None = None
    SilentPush: StrictBool | None = None
    SmallImageIconUrl: StrictStr | None = None
    Sound: StrictStr | None = None
    Substitutions: dict[StrictStr, list[StrictStr]] | None = None
    Title: StrictStr | None = None
    Url: StrictStr | None = None
