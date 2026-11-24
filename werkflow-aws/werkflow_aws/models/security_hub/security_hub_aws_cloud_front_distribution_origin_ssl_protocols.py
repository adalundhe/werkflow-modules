from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubAwsCloudFrontDistributionOriginSslProtocols(BaseModel):
    Items: list[StrictStr] | None = None
    Quantity: StrictInt | None = None
