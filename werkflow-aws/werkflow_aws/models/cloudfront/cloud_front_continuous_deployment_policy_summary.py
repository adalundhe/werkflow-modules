from __future__ import annotations
from pydantic import BaseModel
from .cloud_front_continuous_deployment_policy import CloudFrontContinuousDeploymentPolicy


class CloudFrontContinuousDeploymentPolicySummary(BaseModel):
    ContinuousDeploymentPolicy: CloudFrontContinuousDeploymentPolicy | None = None
