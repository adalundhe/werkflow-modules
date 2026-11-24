from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ResilienceHubListAppComponentCompliancesRequest(BaseModel):
    assessmentArn: StrictStr
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
