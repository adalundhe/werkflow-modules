from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lex_prompt_specification import LexPromptSpecification
from .lex_sample_utterance import LexSampleUtterance
from .lex_slot_capture_setting import LexSlotCaptureSetting
from .lex_slot_default_value_specification import LexSlotDefaultValueSpecification
from .lex_slot_resolution_setting import LexSlotResolutionSetting
from .lex_wait_and_continue_specification import LexWaitAndContinueSpecification


class LexSlotValueElicitationSetting(BaseModel):
    defaultValueSpecification: LexSlotDefaultValueSpecification | None = None
    slotConstraint: StrictStr | None = None
    promptSpecification: LexPromptSpecification | None = None
    sampleUtterances: list[LexSampleUtterance] | None = None
    waitAndContinueSpecification: LexWaitAndContinueSpecification | None = None
    slotCaptureSetting: LexSlotCaptureSetting | None = None
    slotResolutionSetting: LexSlotResolutionSetting | None = None
