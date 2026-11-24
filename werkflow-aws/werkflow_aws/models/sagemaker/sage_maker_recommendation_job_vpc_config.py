from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerRecommendationJobVpcConfig(BaseModel):
    SecurityGroupIds: list[StrictStr] | None = None
    Subnets: list[StrictStr] | None = None
