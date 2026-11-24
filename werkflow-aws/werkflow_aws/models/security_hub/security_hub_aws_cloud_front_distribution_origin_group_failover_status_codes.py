from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SecurityHubAwsCloudFrontDistributionOriginGroupFailoverStatusCodes(BaseModel):
    Items: list[StrictInt] | None = None
    Quantity: StrictInt | None = None
