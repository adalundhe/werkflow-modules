from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .comprehend_key_phrase import ComprehendKeyPhrase


class ComprehendDetectKeyPhrasesResponse(BaseModel):
    KeyPhrases: list[ComprehendKeyPhrase] | None = None
    ResponseMetadata: dict[str, Any] | None = None
