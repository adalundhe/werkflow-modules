from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexDescribeSlotRequest(BaseModel):
    slotId: StrictStr
    botId: StrictStr
    botVersion: StrictStr
    localeId: StrictStr
    intentId: StrictStr
