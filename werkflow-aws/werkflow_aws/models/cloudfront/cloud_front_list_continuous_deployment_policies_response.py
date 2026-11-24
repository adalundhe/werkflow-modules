from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_front_continuous_deployment_policy_list import CloudFrontContinuousDeploymentPolicyList


class CloudFrontListContinuousDeploymentPoliciesResponse(BaseModel):
    ContinuousDeploymentPolicyList: CloudFrontContinuousDeploymentPolicyList | None = None
    ResponseMetadata: dict[str, Any] | None = None
