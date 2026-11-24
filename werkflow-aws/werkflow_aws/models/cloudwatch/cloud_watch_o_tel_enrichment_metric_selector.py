from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchOTelEnrichmentMetricSelector(BaseModel):
    Namespace: StrictStr | None = None
    MetricNames: list[StrictStr] | None = None
