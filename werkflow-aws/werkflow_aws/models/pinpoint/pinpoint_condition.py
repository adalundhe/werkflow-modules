from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_simple_condition import PinpointSimpleCondition


class PinpointCondition(BaseModel):
    Conditions: list[PinpointSimpleCondition] | None = None
    Operator: StrictStr | None = None
