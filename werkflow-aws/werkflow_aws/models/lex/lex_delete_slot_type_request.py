from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class LexDeleteSlotTypeRequest(BaseModel):
    slotTypeId: StrictStr
    botId: StrictStr
    botVersion: StrictStr
    localeId: StrictStr
    skipResourceInUseCheck: StrictBool | None = None
