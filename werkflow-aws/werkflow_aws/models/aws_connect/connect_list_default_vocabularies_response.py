from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_default_vocabulary import ConnectDefaultVocabulary


class ConnectListDefaultVocabulariesResponse(BaseModel):
    DefaultVocabularyList: list[ConnectDefaultVocabulary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
