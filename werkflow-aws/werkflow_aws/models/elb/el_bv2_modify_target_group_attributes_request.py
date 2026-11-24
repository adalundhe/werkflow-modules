from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .el_bv2_target_group_attribute import ELBv2TargetGroupAttribute


class ELBv2ModifyTargetGroupAttributesRequest(BaseModel):
    TargetGroupArn: StrictStr
    Attributes: list[ELBv2TargetGroupAttribute]
