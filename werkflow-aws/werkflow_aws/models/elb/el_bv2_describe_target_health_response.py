from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .el_bv2_target_health_description import ELBv2TargetHealthDescription


class ELBv2DescribeTargetHealthResponse(BaseModel):
    TargetHealthDescriptions: list[ELBv2TargetHealthDescription] | None = None
    ResponseMetadata: dict[str, Any] | None = None
