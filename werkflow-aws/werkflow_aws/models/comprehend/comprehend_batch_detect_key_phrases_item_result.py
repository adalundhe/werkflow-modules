from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .comprehend_key_phrase import ComprehendKeyPhrase


class ComprehendBatchDetectKeyPhrasesItemResult(BaseModel):
    Index: StrictInt | None = None
    KeyPhrases: list[ComprehendKeyPhrase] | None = None
