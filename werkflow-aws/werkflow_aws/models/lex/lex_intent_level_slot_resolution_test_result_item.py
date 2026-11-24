from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .lex_slot_resolution_test_result_item import LexSlotResolutionTestResultItem


class LexIntentLevelSlotResolutionTestResultItem(BaseModel):
    intentName: StrictStr | None = None
    multiTurnConversation: StrictBool | None = None
    slotResolutionResults: list[LexSlotResolutionTestResultItem] | None = None
