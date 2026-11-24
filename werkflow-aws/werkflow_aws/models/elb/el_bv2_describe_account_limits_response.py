from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .el_bv2_limit import ELBv2Limit


class ELBv2DescribeAccountLimitsResponse(BaseModel):
    Limits: list[ELBv2Limit] | None = None
    NextMarker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
