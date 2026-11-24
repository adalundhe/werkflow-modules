from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .sage_maker_inference_component_capacity_size import SageMakerInferenceComponentCapacitySize


class SageMakerInferenceComponentRollingUpdatePolicy(BaseModel):
    MaximumBatchSize: SageMakerInferenceComponentCapacitySize | None = None
    WaitIntervalInSeconds: StrictInt | None = None
    MaximumExecutionTimeoutInSeconds: StrictInt | None = None
    RollbackMaximumBatchSize: SageMakerInferenceComponentCapacitySize | None = None
