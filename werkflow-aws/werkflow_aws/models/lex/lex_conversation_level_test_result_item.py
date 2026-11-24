from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lex_conversation_level_intent_classification_result_item import LexConversationLevelIntentClassificationResultItem
from .lex_conversation_level_slot_resolution_result_item import LexConversationLevelSlotResolutionResultItem


class LexConversationLevelTestResultItem(BaseModel):
    conversationId: StrictStr | None = None
    endToEndResult: StrictStr | None = None
    speechTranscriptionResult: StrictStr | None = None
    intentClassificationResults: list[LexConversationLevelIntentClassificationResultItem] | None = None
    slotResolutionResults: list[LexConversationLevelSlotResolutionResultItem] | None = None
