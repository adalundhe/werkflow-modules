from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexStartBotResourceGenerationRequest(BaseModel):
    generationInputPrompt: StrictStr
    botId: StrictStr
    botVersion: StrictStr
    localeId: StrictStr
