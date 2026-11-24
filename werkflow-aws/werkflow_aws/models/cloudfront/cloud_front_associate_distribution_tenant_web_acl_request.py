from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontAssociateDistributionTenantWebACLRequest(BaseModel):
    Id: StrictStr
    WebACLArn: StrictStr
    IfMatch: StrictStr | None = None
