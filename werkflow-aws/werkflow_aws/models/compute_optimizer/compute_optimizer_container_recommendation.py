from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .compute_optimizer_memory_size_configuration import ComputeOptimizerMemorySizeConfiguration


class ComputeOptimizerContainerRecommendation(BaseModel):
    containerName: StrictStr | None = None
    memorySizeConfiguration: ComputeOptimizerMemorySizeConfiguration | None = None
    cpu: StrictInt | None = None
