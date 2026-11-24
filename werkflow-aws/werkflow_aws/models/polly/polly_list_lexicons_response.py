from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .polly_lexicon_description import PollyLexiconDescription


class PollyListLexiconsResponse(BaseModel):
    Lexicons: list[PollyLexiconDescription] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
