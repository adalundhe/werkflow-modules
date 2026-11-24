from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .lex_allowed_input_types import LexAllowedInputTypes
from .lex_audio_and_dtmf_input_specification import LexAudioAndDTMFInputSpecification
from .lex_text_input_specification import LexTextInputSpecification


class LexPromptAttemptSpecification(BaseModel):
    allowInterrupt: StrictBool | None = None
    allowedInputTypes: LexAllowedInputTypes | None = None
    audioAndDTMFInputSpecification: LexAudioAndDTMFInputSpecification | None = None
    textInputSpecification: LexTextInputSpecification | None = None
