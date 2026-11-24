from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexDescribeBotResourceGenerationRequest(BaseModel):
    botId: StrictStr
    botVersion: StrictStr
    localeId: StrictStr
    generationId: StrictStr
