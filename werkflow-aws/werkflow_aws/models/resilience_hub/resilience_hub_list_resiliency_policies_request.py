from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ResilienceHubListResiliencyPoliciesRequest(BaseModel):
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
    policyName: StrictStr | None = None
