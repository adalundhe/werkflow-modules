from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .quick_sight_named_entity_definition_metric import QuickSightNamedEntityDefinitionMetric


class QuickSightNamedEntityDefinition(BaseModel):
    FieldName: StrictStr | None = None
    PropertyName: StrictStr | None = None
    PropertyRole: StrictStr | None = None
    PropertyUsage: StrictStr | None = None
    Metric: QuickSightNamedEntityDefinitionMetric | None = None
    RankOrder: StrictInt | None = None
    PresentationOrder: StrictInt | None = None
    IsHidden: StrictBool | None = None
