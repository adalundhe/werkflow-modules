from __future__ import annotations
from pydantic import BaseModel
from .lex_conversation_level_test_result_item import LexConversationLevelTestResultItem


class LexConversationLevelTestResults(BaseModel):
    items: list[LexConversationLevelTestResultItem] | None = None
