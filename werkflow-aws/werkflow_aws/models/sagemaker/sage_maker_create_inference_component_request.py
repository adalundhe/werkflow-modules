from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_inference_component_runtime_config import SageMakerInferenceComponentRuntimeConfig
from .sage_maker_inference_component_specification import SageMakerInferenceComponentSpecification
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerCreateInferenceComponentRequest(BaseModel):
    InferenceComponentName: StrictStr
    EndpointName: StrictStr
    VariantName: StrictStr | None = None
    Specification: SageMakerInferenceComponentSpecification | None = None
    Specifications: list[SageMakerInferenceComponentSpecification] | None = None
    RuntimeConfig: SageMakerInferenceComponentRuntimeConfig | None = None
    Tags: list[SageMakerTagModel] | None = None
