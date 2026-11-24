from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ServiceCatalogProductViewAggregationValue(BaseModel):
    Value: StrictStr | None = None
    ApproximateCount: StrictInt | None = None
