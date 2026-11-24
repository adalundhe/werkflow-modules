from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_front_continuous_deployment_single_header_config import CloudFrontContinuousDeploymentSingleHeaderConfig
from .cloud_front_continuous_deployment_single_weight_config import CloudFrontContinuousDeploymentSingleWeightConfig


class CloudFrontTrafficConfig(BaseModel):
    SingleWeightConfig: CloudFrontContinuousDeploymentSingleWeightConfig | None = None
    SingleHeaderConfig: CloudFrontContinuousDeploymentSingleHeaderConfig | None = None
    Type: StrictStr | None = None
