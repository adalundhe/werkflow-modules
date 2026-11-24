from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class CloudFrontAssociateDistributionTenantWebACLResponse(BaseModel):
    Id: StrictStr | None = None
    WebACLArn: StrictStr | None = None
    ETag: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
