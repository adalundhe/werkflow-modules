from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontDeleteContinuousDeploymentPolicyRequest(BaseModel):
    Id: StrictStr
    IfMatch: StrictStr | None = None
