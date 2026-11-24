from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .el_bv2_rule import ELBv2Rule


class ELBv2SetRulePrioritiesResponse(BaseModel):
    Rules: list[ELBv2Rule] | None = None
    ResponseMetadata: dict[str, Any] | None = None
