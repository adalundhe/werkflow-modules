from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .el_bv2_target_group import ELBv2TargetGroup


class ELBv2ModifyTargetGroupResponse(BaseModel):
    TargetGroups: list[ELBv2TargetGroup] | None = None
    ResponseMetadata: dict[str, Any] | None = None
