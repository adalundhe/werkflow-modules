from __future__ import annotations
from pydantic import BaseModel
from .lex_prompt_specification import LexPromptSpecification
from .lex_sample_utterance import LexSampleUtterance
from .lex_slot_default_value_specification import LexSlotDefaultValueSpecification
from .lex_wait_and_continue_specification import LexWaitAndContinueSpecification


class LexSubSlotValueElicitationSetting(BaseModel):
    defaultValueSpecification: LexSlotDefaultValueSpecification | None = None
    promptSpecification: LexPromptSpecification | None = None
    sampleUtterances: list[LexSampleUtterance] | None = None
    waitAndContinueSpecification: LexWaitAndContinueSpecification | None = None
