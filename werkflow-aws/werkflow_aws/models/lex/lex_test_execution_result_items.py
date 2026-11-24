from __future__ import annotations
from pydantic import BaseModel
from .lex_conversation_level_test_results import LexConversationLevelTestResults
from .lex_intent_classification_test_results import LexIntentClassificationTestResults
from .lex_intent_level_slot_resolution_test_results import LexIntentLevelSlotResolutionTestResults
from .lex_overall_test_results import LexOverallTestResults
from .lex_utterance_level_test_results import LexUtteranceLevelTestResults


class LexTestExecutionResultItems(BaseModel):
    overallTestResults: LexOverallTestResults | None = None
    conversationLevelTestResults: LexConversationLevelTestResults | None = None
    intentClassificationTestResults: LexIntentClassificationTestResults | None = None
    intentLevelSlotResolutionTestResults: LexIntentLevelSlotResolutionTestResults | None = None
    utteranceLevelTestResults: LexUtteranceLevelTestResults | None = None
