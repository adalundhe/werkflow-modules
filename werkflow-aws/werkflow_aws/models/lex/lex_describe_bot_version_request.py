from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexDescribeBotVersionRequest(BaseModel):
    botId: StrictStr
    botVersion: StrictStr
