from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .sage_maker_property_name_suggestion import SageMakerPropertyNameSuggestion


class SageMakerGetSearchSuggestionsResponse(BaseModel):
    PropertyNameSuggestions: list[SageMakerPropertyNameSuggestion] | None = None
    ResponseMetadata: dict[str, Any] | None = None
