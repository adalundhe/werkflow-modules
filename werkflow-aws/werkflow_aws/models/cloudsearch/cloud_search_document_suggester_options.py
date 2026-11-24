from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudSearchDocumentSuggesterOptions(BaseModel):
    SourceField: StrictStr | None = None
    FuzzyMatching: StrictStr | None = None
    SortExpression: StrictStr | None = None
