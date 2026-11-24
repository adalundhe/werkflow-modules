from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .lex_message_group import LexMessageGroup
from .lex_prompt_attempt_specification import LexPromptAttemptSpecification


class LexPromptSpecification(BaseModel):
    messageGroups: list[LexMessageGroup] | None = None
    maxRetries: StrictInt | None = None
    allowInterrupt: StrictBool | None = None
    messageSelectionStrategy: StrictStr | None = None
    promptAttemptsSpecification: dict[StrictStr, LexPromptAttemptSpecification] | None = None
