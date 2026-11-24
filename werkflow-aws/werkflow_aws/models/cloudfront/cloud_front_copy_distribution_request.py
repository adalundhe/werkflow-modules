from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CloudFrontCopyDistributionRequest(BaseModel):
    PrimaryDistributionId: StrictStr
    CallerReference: StrictStr
    Staging: StrictBool | None = None
    IfMatch: StrictStr | None = None
    Enabled: StrictBool | None = None
