from __future__ import annotations
from pydantic import BaseModel
from .fms_policy import FMSPolicy
from .fms_tag import FMSTag


class FMSPutPolicyRequest(BaseModel):
    Policy: FMSPolicy
    TagList: list[FMSTag] | None = None
