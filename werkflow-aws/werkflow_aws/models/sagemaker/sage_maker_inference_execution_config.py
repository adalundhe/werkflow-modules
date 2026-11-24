from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_inference_execution_mode import SageMakerInferenceExecutionMode


class SageMakerInferenceExecutionConfig(BaseModel):
    Mode: SageMakerInferenceExecutionMode | None = None
