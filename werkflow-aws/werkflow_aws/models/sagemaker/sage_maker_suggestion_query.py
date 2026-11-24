from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_property_name_query import SageMakerPropertyNameQuery


class SageMakerSuggestionQuery(BaseModel):
    PropertyNameQuery: SageMakerPropertyNameQuery | None = None
