from __future__ import annotations
from pydantic import BaseModel
from .lex_test_set_intent_discrepancy_item import LexTestSetIntentDiscrepancyItem
from .lex_test_set_slot_discrepancy_item import LexTestSetSlotDiscrepancyItem


class LexTestSetDiscrepancyErrors(BaseModel):
    intentDiscrepancies: list[LexTestSetIntentDiscrepancyItem] | None = None
    slotDiscrepancies: list[LexTestSetSlotDiscrepancyItem] | None = None
