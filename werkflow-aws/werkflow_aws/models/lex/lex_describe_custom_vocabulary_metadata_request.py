from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexDescribeCustomVocabularyMetadataRequest(BaseModel):
    botId: StrictStr
    botVersion: StrictStr
    localeId: StrictStr
