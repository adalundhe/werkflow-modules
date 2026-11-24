from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .el_bv2_rule import ELBv2Rule


class ELBv2DescribeRulesResponse(BaseModel):
    Rules: list[ELBv2Rule] | None = None
    NextMarker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
