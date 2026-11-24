from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .lex_intent_classification_test_result_item_counts import LexIntentClassificationTestResultItemCounts


class LexIntentClassificationTestResultItem(BaseModel):
    intentName: StrictStr | None = None
    multiTurnConversation: StrictBool | None = None
    resultCounts: LexIntentClassificationTestResultItemCounts | None = None
