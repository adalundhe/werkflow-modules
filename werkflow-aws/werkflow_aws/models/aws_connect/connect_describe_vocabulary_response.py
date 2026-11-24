from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .connect_vocabulary import ConnectVocabulary


class ConnectDescribeVocabularyResponse(BaseModel):
    Vocabulary: ConnectVocabulary | None = None
    ResponseMetadata: dict[str, Any] | None = None
