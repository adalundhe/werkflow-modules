from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .el_bv2_target_group_attribute import ELBv2TargetGroupAttribute


class ELBv2ModifyTargetGroupAttributesResponse(BaseModel):
    Attributes: list[ELBv2TargetGroupAttribute] | None = None
    ResponseMetadata: dict[str, Any] | None = None
