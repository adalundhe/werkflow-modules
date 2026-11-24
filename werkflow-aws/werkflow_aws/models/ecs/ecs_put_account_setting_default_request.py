from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ECSPutAccountSettingDefaultRequest(BaseModel):
    name: Literal['serviceLongArnFormat', 'taskLongArnFormat', 'containerInstanceLongArnFormat', 'awsvpcTrunking', 'containerInsights', 'fargateFIPSMode', 'tagResourceAuthorization', 'fargateTaskRetirementWaitPeriod', 'guardDutyActivate', 'defaultLogDriverMode', 'fargateEventWindows']
    value: StrictStr
