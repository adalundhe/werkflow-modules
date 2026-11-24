from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_named_entity_definition import QuickSightNamedEntityDefinition
from .quick_sight_named_entity_sort import QuickSightNamedEntitySort
from .quick_sight_semantic_entity_type import QuickSightSemanticEntityType


class QuickSightTopicNamedEntity(BaseModel):
    EntityName: StrictStr | None = None
    EntityDescription: StrictStr | None = None
    EntitySynonyms: list[StrictStr] | None = None
    SemanticEntityType: QuickSightSemanticEntityType | None = None
    Definition: list[QuickSightNamedEntityDefinition] | None = None
    Sort: list[QuickSightNamedEntitySort] | None = None
    RankOrder: StrictInt | None = None
    PresentationOrder: StrictInt | None = None
