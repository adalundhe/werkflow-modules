from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class CloudFrontDisassociateDistributionTenantWebACLResponse(BaseModel):
    Id: StrictStr | None = None
    ETag: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
