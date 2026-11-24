from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .kendra_suggestion import KendraSuggestion


class KendraGetQuerySuggestionsResponse(BaseModel):
    QuerySuggestionsId: StrictStr | None = None
    Suggestions: list[KendraSuggestion] | None = None
    ResponseMetadata: dict[str, Any] | None = None
