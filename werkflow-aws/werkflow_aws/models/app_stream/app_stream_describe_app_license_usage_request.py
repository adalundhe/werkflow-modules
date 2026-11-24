from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AppStreamDescribeAppLicenseUsageRequest(BaseModel):
    BillingPeriod: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
