from __future__ import annotations
from pydantic import BaseModel
from .lex_intent_classification_test_result_item import LexIntentClassificationTestResultItem


class LexIntentClassificationTestResults(BaseModel):
    items: list[LexIntentClassificationTestResultItem] | None = None
