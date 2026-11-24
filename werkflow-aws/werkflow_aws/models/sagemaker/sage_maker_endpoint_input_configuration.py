from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_environment_parameter_ranges import SageMakerEnvironmentParameterRanges
from .sage_maker_production_variant_serverless_config_model import SageMakerProductionVariantServerlessConfigModel


class SageMakerEndpointInputConfiguration(BaseModel):
    InstanceType: StrictStr | None = None
    ServerlessConfig: SageMakerProductionVariantServerlessConfigModel | None = None
    InferenceSpecificationName: StrictStr | None = None
    EnvironmentParameterRanges: SageMakerEnvironmentParameterRanges | None = None
