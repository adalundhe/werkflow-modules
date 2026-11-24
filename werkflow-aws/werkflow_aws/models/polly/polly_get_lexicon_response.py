from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .polly_lexicon import PollyLexicon
from .polly_lexicon_attributes import PollyLexiconAttributes


class PollyGetLexiconResponse(BaseModel):
    Lexicon: PollyLexicon | None = None
    LexiconAttributes: PollyLexiconAttributes | None = None
    ResponseMetadata: dict[str, Any] | None = None
