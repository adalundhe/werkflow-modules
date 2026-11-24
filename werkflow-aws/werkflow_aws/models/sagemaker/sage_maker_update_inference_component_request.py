from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_inference_component_deployment_config import SageMakerInferenceComponentDeploymentConfig
from .sage_maker_inference_component_runtime_config import SageMakerInferenceComponentRuntimeConfig
from .sage_maker_inference_component_specification import SageMakerInferenceComponentSpecification


class SageMakerUpdateInferenceComponentRequest(BaseModel):
    InferenceComponentName: StrictStr
    Specification: SageMakerInferenceComponentSpecification | None = None
    Specifications: list[SageMakerInferenceComponentSpecification] | None = None
    RuntimeConfig: SageMakerInferenceComponentRuntimeConfig | None = None
    DeploymentConfig: SageMakerInferenceComponentDeploymentConfig | None = None
