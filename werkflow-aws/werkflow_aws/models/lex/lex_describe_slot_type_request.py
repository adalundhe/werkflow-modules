from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexDescribeSlotTypeRequest(BaseModel):
    slotTypeId: StrictStr
    botId: StrictStr
    botVersion: StrictStr
    localeId: StrictStr
