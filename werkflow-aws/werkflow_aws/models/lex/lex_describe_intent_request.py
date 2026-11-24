from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexDescribeIntentRequest(BaseModel):
    intentId: StrictStr
    botId: StrictStr
    botVersion: StrictStr
    localeId: StrictStr
