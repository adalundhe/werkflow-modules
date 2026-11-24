from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightNamedEntityDefinitionMetric(BaseModel):
    Aggregation: StrictStr | None = None
    AggregationFunctionParameters: dict[StrictStr, StrictStr] | None = None
