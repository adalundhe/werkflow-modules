from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lex_utterance_audio_input_specification import LexUtteranceAudioInputSpecification


class LexUtteranceInputSpecification(BaseModel):
    textInput: StrictStr | None = None
    audioInput: LexUtteranceAudioInputSpecification | None = None
