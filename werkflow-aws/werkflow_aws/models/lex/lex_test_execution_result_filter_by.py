from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .lex_conversation_level_test_results_filter_by import LexConversationLevelTestResultsFilterBy


class LexTestExecutionResultFilterBy(BaseModel):
    resultTypeFilter: Literal['OverallTestResults', 'ConversationLevelTestResults', 'IntentClassificationTestResults', 'SlotResolutionTestResults', 'UtteranceLevelResults']
    conversationLevelTestResultsFilterBy: LexConversationLevelTestResultsFilterBy | None = None
