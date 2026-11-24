from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubDescribeProductsRequest(BaseModel):
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    ProductArn: StrictStr | None = None
