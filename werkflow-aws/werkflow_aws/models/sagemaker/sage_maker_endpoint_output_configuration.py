from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_production_variant_serverless_config_model import SageMakerProductionVariantServerlessConfigModel


class SageMakerEndpointOutputConfiguration(BaseModel):
    EndpointName: StrictStr | None = None
    VariantName: StrictStr | None = None
    InstanceType: StrictStr | None = None
    InitialInstanceCount: StrictInt | None = None
    ServerlessConfig: SageMakerProductionVariantServerlessConfigModel | None = None
