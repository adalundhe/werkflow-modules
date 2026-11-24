from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_inference_component_runtime_config import SageMakerInferenceComponentRuntimeConfig


class SageMakerUpdateInferenceComponentRuntimeConfigRequest(BaseModel):
    InferenceComponentName: StrictStr
    DesiredRuntimeConfig: SageMakerInferenceComponentRuntimeConfig
