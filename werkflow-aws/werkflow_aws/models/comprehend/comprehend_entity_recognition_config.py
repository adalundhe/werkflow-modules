from __future__ import annotations
from pydantic import BaseModel
from .comprehend_entity_types_list_item import ComprehendEntityTypesListItem


class ComprehendEntityRecognitionConfig(BaseModel):
    EntityTypes: list[ComprehendEntityTypesListItem] | None = None
