from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TranslateDescribeTextTranslationJobRequest(BaseModel):
    JobId: StrictStr
