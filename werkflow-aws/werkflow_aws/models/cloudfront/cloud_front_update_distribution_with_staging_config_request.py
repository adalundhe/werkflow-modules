from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontUpdateDistributionWithStagingConfigRequest(BaseModel):
    Id: StrictStr
    StagingDistributionId: StrictStr | None = None
    IfMatch: StrictStr | None = None
