from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class ConfigServiceListDiscoveredResourcesRequest(BaseModel):
    resourceType: StrictStr
    resourceIds: list[StrictStr] | None = None
    resourceName: StrictStr | None = None
    limit: StrictInt | None = None
    includeDeletedResources: StrictBool | None = None
    nextToken: StrictStr | None = None
