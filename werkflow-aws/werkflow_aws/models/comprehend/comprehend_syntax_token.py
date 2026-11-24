from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .comprehend_part_of_speech_tag import ComprehendPartOfSpeechTag


class ComprehendSyntaxToken(BaseModel):
    TokenId: StrictInt | None = None
    Text: StrictStr | None = None
    BeginOffset: StrictInt | None = None
    EndOffset: StrictInt | None = None
    PartOfSpeech: ComprehendPartOfSpeechTag | None = None
