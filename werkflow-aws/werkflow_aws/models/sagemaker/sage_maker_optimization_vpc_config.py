from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerOptimizationVpcConfig(BaseModel):
    SecurityGroupIds: list[StrictStr] | None = None
    Subnets: list[StrictStr] | None = None
