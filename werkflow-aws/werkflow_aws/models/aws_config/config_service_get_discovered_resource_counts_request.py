from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ConfigServiceGetDiscoveredResourceCountsRequest(BaseModel):
    resourceTypes: list[StrictStr] | None = None
    limit: StrictInt | None = None
    nextToken: StrictStr | None = None
