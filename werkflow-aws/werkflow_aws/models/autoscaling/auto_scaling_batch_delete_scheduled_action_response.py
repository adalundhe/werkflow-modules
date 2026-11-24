from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .auto_scaling_failed_scheduled_update_group_action_request import AutoScalingFailedScheduledUpdateGroupActionRequest


class AutoScalingBatchDeleteScheduledActionResponse(BaseModel):
    FailedScheduledActions: list[AutoScalingFailedScheduledUpdateGroupActionRequest] | None = None
    ResponseMetadata: dict[str, Any] | None = None
