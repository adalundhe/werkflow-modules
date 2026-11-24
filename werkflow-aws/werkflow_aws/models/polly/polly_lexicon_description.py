from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .polly_lexicon_attributes import PollyLexiconAttributes


class PollyLexiconDescription(BaseModel):
    Name: StrictStr | None = None
    Attributes: PollyLexiconAttributes | None = None
