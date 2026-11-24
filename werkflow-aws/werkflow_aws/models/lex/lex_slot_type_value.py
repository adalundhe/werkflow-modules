from __future__ import annotations
from pydantic import BaseModel
from .lex_sample_value import LexSampleValue


class LexSlotTypeValue(BaseModel):
    sampleValue: LexSampleValue | None = None
    synonyms: list[LexSampleValue] | None = None
