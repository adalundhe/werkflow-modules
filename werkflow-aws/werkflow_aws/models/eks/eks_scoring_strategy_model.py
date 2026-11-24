from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .eks_resource_weight_model import EKSResourceWeightModel


class EKSScoringStrategyModel(BaseModel):
    type: StrictStr | None = None
    resources: list[EKSResourceWeightModel] | None = None
