from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .fms_violation_detail import FMSViolationDetail


class FMSGetViolationDetailsResponse(BaseModel):
    ViolationDetail: FMSViolationDetail | None = None
    ResponseMetadata: dict[str, Any] | None = None
