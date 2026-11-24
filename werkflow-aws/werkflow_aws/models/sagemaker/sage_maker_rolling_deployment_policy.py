from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_capacity_size_config import SageMakerCapacitySizeConfig


class SageMakerRollingDeploymentPolicy(BaseModel):
    MaximumBatchSize: SageMakerCapacitySizeConfig | None = None
    RollbackMaximumBatchSize: SageMakerCapacitySizeConfig | None = None
