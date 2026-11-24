from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_multi_conditional_branch import PinpointMultiConditionalBranch
from .pinpoint_wait_time import PinpointWaitTime


class PinpointMultiConditionalSplitActivity(BaseModel):
    Branches: list[PinpointMultiConditionalBranch] | None = None
    DefaultActivity: StrictStr | None = None
    EvaluationWaitTime: PinpointWaitTime | None = None
