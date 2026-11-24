from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kendra_attribute_filter import KendraAttributeFilter
from .kendra_user_context import KendraUserContext


class KendraAttributeSuggestionsGetConfig(BaseModel):
    SuggestionAttributes: list[StrictStr] | None = None
    AdditionalResponseAttributes: list[StrictStr] | None = None
    AttributeFilter: KendraAttributeFilter | None = None
    UserContext: KendraUserContext | None = None
