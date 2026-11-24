from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontGetContinuousDeploymentPolicyRequest(BaseModel):
    Id: StrictStr
