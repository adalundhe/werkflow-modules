from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_front_continuous_deployment_policy import CloudFrontContinuousDeploymentPolicy


class CloudFrontCreateContinuousDeploymentPolicyResponse(BaseModel):
    ContinuousDeploymentPolicy: CloudFrontContinuousDeploymentPolicy | None = None
    Location: StrictStr | None = None
    ETag: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
