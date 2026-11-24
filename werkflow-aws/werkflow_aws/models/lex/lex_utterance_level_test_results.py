from __future__ import annotations
from pydantic import BaseModel
from .lex_utterance_level_test_result_item import LexUtteranceLevelTestResultItem


class LexUtteranceLevelTestResults(BaseModel):
    items: list[LexUtteranceLevelTestResultItem] | None = None
