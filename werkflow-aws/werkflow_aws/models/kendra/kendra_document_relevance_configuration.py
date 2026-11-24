from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kendra_relevance import KendraRelevance


class KendraDocumentRelevanceConfiguration(BaseModel):
    Name: StrictStr
    Relevance: KendraRelevance
