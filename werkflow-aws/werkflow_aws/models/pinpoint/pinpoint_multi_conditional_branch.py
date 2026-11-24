from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_simple_condition import PinpointSimpleCondition


class PinpointMultiConditionalBranch(BaseModel):
    Condition: PinpointSimpleCondition | None = None
    NextActivity: StrictStr | None = None
