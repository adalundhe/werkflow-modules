from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerTimeSeriesTransformations(BaseModel):
    Filling: dict[StrictStr, dict[StrictStr, StrictStr]] | None = None
    Aggregation: dict[StrictStr, StrictStr] | None = None
