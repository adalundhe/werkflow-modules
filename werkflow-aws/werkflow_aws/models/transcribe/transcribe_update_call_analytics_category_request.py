from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .transcribe_rule import TranscribeRule


class TranscribeUpdateCallAnalyticsCategoryRequest(BaseModel):
    CategoryName: StrictStr
    Rules: list[TranscribeRule]
    InputType: Literal['REAL_TIME', 'POST_CALL'] | None = None
