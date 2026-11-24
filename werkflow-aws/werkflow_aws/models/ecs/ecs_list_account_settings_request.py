from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class ECSListAccountSettingsRequest(BaseModel):
    name: Literal['serviceLongArnFormat', 'taskLongArnFormat', 'containerInstanceLongArnFormat', 'awsvpcTrunking', 'containerInsights', 'fargateFIPSMode', 'tagResourceAuthorization', 'fargateTaskRetirementWaitPeriod', 'guardDutyActivate', 'defaultLogDriverMode', 'fargateEventWindows'] | None = None
    value: StrictStr | None = None
    principalArn: StrictStr | None = None
    effectiveSettings: StrictBool | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
