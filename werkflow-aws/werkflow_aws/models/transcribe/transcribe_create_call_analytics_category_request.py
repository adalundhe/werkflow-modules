from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .transcribe_rule import TranscribeRule
from .transcribe_tag import TranscribeTag


class TranscribeCreateCallAnalyticsCategoryRequest(BaseModel):
    CategoryName: StrictStr
    Rules: list[TranscribeRule]
    Tags: list[TranscribeTag] | None = None
    InputType: Literal['REAL_TIME', 'POST_CALL'] | None = None
