from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lex_conversation_level_result_detail import LexConversationLevelResultDetail
from .lex_execution_error_details import LexExecutionErrorDetails
from .lex_user_turn_input_specification import LexUserTurnInputSpecification
from .lex_user_turn_output_specification import LexUserTurnOutputSpecification


class LexUserTurnResult(BaseModel):
    input: LexUserTurnInputSpecification | None = None
    expectedOutput: LexUserTurnOutputSpecification | None = None
    actualOutput: LexUserTurnOutputSpecification | None = None
    errorDetails: LexExecutionErrorDetails | None = None
    endToEndResult: StrictStr | None = None
    intentMatchResult: StrictStr | None = None
    slotMatchResult: StrictStr | None = None
    speechTranscriptionResult: StrictStr | None = None
    conversationLevelResult: LexConversationLevelResultDetail | None = None
