from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .cloud_front_continuous_deployment_policy_config import CloudFrontContinuousDeploymentPolicyConfig


class CloudFrontContinuousDeploymentPolicy(BaseModel):
    Id: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    ContinuousDeploymentPolicyConfig: CloudFrontContinuousDeploymentPolicyConfig | None = None
