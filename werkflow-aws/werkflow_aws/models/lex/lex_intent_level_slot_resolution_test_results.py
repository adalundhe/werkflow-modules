from __future__ import annotations
from pydantic import BaseModel
from .lex_intent_level_slot_resolution_test_result_item import LexIntentLevelSlotResolutionTestResultItem


class LexIntentLevelSlotResolutionTestResults(BaseModel):
    items: list[LexIntentLevelSlotResolutionTestResultItem] | None = None
