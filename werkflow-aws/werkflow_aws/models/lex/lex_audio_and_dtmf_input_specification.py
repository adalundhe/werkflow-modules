from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .lex_audio_specification import LexAudioSpecification
from .lex_dtmf_specification import LexDTMFSpecification


class LexAudioAndDTMFInputSpecification(BaseModel):
    startTimeoutMs: StrictInt | None = None
    audioSpecification: LexAudioSpecification | None = None
    dtmfSpecification: LexDTMFSpecification | None = None
