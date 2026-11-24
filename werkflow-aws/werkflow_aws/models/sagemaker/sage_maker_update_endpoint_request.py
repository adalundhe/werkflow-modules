from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .sage_maker_deployment_config import SageMakerDeploymentConfig
from .sage_maker_variant_property import SageMakerVariantProperty


class SageMakerUpdateEndpointRequest(BaseModel):
    EndpointName: StrictStr
    EndpointConfigName: StrictStr
    RetainAllVariantProperties: StrictBool | None = None
    ExcludeRetainedVariantProperties: list[SageMakerVariantProperty] | None = None
    DeploymentConfig: SageMakerDeploymentConfig | None = None
    RetainDeploymentConfig: StrictBool | None = None
