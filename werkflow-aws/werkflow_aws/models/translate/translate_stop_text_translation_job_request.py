from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TranslateStopTextTranslationJobRequest(BaseModel):
    JobId: StrictStr
