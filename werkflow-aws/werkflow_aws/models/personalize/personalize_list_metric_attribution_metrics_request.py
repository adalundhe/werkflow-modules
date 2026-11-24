from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class PersonalizeListMetricAttributionMetricsRequest(BaseModel):
    metricAttributionArn: StrictStr | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
