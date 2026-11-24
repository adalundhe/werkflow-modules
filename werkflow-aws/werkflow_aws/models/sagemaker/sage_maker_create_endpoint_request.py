from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_deployment_config import SageMakerDeploymentConfig
from .sage_maker_tag import SageMakerTag


class SageMakerCreateEndpointRequest(BaseModel):
    EndpointName: StrictStr
    EndpointConfigName: StrictStr
    DeploymentConfig: SageMakerDeploymentConfig | None = None
    Tags: list[SageMakerTag] | None = None
