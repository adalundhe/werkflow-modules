from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_front_continuous_deployment_policy_config import CloudFrontContinuousDeploymentPolicyConfig


class CloudFrontUpdateContinuousDeploymentPolicyRequest(BaseModel):
    ContinuousDeploymentPolicyConfig: CloudFrontContinuousDeploymentPolicyConfig
    Id: StrictStr
    IfMatch: StrictStr | None = None
