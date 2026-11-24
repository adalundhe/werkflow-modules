from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .kendra_attribute_suggestions_get_config import KendraAttributeSuggestionsGetConfig


class KendraGetQuerySuggestionsRequest(BaseModel):
    IndexId: StrictStr
    QueryText: StrictStr
    MaxSuggestionsCount: StrictInt | None = None
    SuggestionTypes: list[Literal['QUERY', 'DOCUMENT_ATTRIBUTES']] | None = None
    AttributeSuggestionsConfig: KendraAttributeSuggestionsGetConfig | None = None
