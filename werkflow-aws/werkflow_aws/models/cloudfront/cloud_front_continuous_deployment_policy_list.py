from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .cloud_front_continuous_deployment_policy_summary import CloudFrontContinuousDeploymentPolicySummary


class CloudFrontContinuousDeploymentPolicyList(BaseModel):
    NextMarker: StrictStr | None = None
    MaxItems: StrictInt | None = None
    Quantity: StrictInt | None = None
    Items: list[CloudFrontContinuousDeploymentPolicySummary] | None = None
