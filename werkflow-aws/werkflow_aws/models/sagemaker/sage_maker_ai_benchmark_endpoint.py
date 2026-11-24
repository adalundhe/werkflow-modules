from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_ai_benchmark_inference_component import SageMakerAIBenchmarkInferenceComponent


class SageMakerAIBenchmarkEndpoint(BaseModel):
    Identifier: StrictStr | None = None
    TargetContainerHostname: StrictStr | None = None
    InferenceComponents: list[SageMakerAIBenchmarkInferenceComponent] | None = None
