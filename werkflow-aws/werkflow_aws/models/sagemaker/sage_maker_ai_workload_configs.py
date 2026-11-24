from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_workload_spec import SageMakerWorkloadSpec


class SageMakerAIWorkloadConfigs(BaseModel):
    WorkloadSpec: SageMakerWorkloadSpec | None = None
