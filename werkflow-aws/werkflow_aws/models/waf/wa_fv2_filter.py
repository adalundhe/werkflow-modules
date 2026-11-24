from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .wa_fv2_condition import WAFv2Condition


class WAFv2Filter(BaseModel):
    Behavior: StrictStr | None = None
    Requirement: StrictStr | None = None
    Conditions: list[WAFv2Condition] | None = None
