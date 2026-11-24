from __future__ import annotations
from pydantic import BaseModel
from .el_bv2_target_group_stickiness_config import ELBv2TargetGroupStickinessConfig
from .el_bv2_target_group_tuple import ELBv2TargetGroupTuple


class ELBv2ForwardActionConfig(BaseModel):
    TargetGroups: list[ELBv2TargetGroupTuple] | None = None
    TargetGroupStickinessConfig: ELBv2TargetGroupStickinessConfig | None = None
