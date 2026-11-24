from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexDeleteCustomVocabularyRequest(BaseModel):
    botId: StrictStr
    botVersion: StrictStr
    localeId: StrictStr
