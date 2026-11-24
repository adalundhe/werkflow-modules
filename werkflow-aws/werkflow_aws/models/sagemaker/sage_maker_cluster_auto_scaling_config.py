from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class SageMakerClusterAutoScalingConfig(BaseModel):
    Mode: Literal['Enable', 'Disable']
    AutoScalerType: Literal['Karpenter'] | None = None
