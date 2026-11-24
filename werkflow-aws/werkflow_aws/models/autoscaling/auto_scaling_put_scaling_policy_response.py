from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .auto_scaling_alarm import AutoScalingAlarm


class AutoScalingPutScalingPolicyResponse(BaseModel):
    PolicyARN: StrictStr | None = None
    Alarms: list[AutoScalingAlarm] | None = None
    ResponseMetadata: dict[str, Any] | None = None
