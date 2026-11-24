from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .wa_fv2_rule import WAFv2Rule


class WAFv2CheckCapacityRequest(BaseModel):
    Scope: Literal['CLOUDFRONT', 'REGIONAL']
    Rules: list[WAFv2Rule]
