from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kendra_relevance import KendraRelevance
from .kendra_search import KendraSearch


class KendraDocumentMetadataConfiguration(BaseModel):
    Name: StrictStr | None = None
    Type: StrictStr | None = None
    Relevance: KendraRelevance | None = None
    Search: KendraSearch | None = None
