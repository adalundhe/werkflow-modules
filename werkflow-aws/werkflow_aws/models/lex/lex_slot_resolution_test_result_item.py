from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lex_slot_resolution_test_result_item_counts import LexSlotResolutionTestResultItemCounts


class LexSlotResolutionTestResultItem(BaseModel):
    slotName: StrictStr | None = None
    resultCounts: LexSlotResolutionTestResultItemCounts | None = None
