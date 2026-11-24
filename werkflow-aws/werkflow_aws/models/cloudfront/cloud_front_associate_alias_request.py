from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontAssociateAliasRequest(BaseModel):
    TargetDistributionId: StrictStr
    Alias: StrictStr
