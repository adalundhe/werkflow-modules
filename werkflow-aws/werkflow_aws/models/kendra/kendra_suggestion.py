from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kendra_source_document import KendraSourceDocument
from .kendra_suggestion_value import KendraSuggestionValue


class KendraSuggestion(BaseModel):
    Id: StrictStr | None = None
    Value: KendraSuggestionValue | None = None
    SourceDocuments: list[KendraSourceDocument] | None = None
