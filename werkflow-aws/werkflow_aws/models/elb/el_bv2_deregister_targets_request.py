from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .el_bv2_target_description import ELBv2TargetDescription


class ELBv2DeregisterTargetsRequest(BaseModel):
    TargetGroupArn: StrictStr
    Targets: list[ELBv2TargetDescription]
