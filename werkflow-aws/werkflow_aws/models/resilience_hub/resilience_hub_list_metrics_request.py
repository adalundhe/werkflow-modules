from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .resilience_hub_condition import ResilienceHubCondition
from .resilience_hub_field import ResilienceHubField
from .resilience_hub_sort import ResilienceHubSort


class ResilienceHubListMetricsRequest(BaseModel):
    conditions: list[ResilienceHubCondition] | None = None
    dataSource: StrictStr | None = None
    fields: list[ResilienceHubField] | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
    sorts: list[ResilienceHubSort] | None = None
