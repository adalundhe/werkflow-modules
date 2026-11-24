from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TranscribeDescribeLanguageModelRequest(BaseModel):
    ModelName: StrictStr
