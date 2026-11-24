from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .el_bv2_target_description import ELBv2TargetDescription


class ELBv2DescribeTargetHealthRequest(BaseModel):
    TargetGroupArn: StrictStr
    Targets: list[ELBv2TargetDescription] | None = None
    Include: list[Literal['AnomalyDetection', 'All']] | None = None
