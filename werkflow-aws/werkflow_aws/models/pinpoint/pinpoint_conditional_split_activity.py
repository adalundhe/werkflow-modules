from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_condition import PinpointCondition
from .pinpoint_wait_time import PinpointWaitTime


class PinpointConditionalSplitActivity(BaseModel):
    Condition: PinpointCondition | None = None
    EvaluationWaitTime: PinpointWaitTime | None = None
    FalseActivity: StrictStr | None = None
    TrueActivity: StrictStr | None = None
