from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IoTListSecurityProfilesRequest(BaseModel):
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
    dimensionName: StrictStr | None = None
    metricName: StrictStr | None = None
