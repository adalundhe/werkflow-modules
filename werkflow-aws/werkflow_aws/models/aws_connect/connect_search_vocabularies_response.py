from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_vocabulary_summary import ConnectVocabularySummary


class ConnectSearchVocabulariesResponse(BaseModel):
    VocabularySummaryList: list[ConnectVocabularySummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
