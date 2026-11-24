from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .el_bv2_target_group import ELBv2TargetGroup


class ELBv2DescribeTargetGroupsResponse(BaseModel):
    TargetGroups: list[ELBv2TargetGroup] | None = None
    NextMarker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
