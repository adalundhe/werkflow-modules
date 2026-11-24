from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .auto_scaling_scheduled_update_group_action import AutoScalingScheduledUpdateGroupAction


class AutoScalingDescribeScheduledActionsResponse(BaseModel):
    ScheduledUpdateGroupActions: list[AutoScalingScheduledUpdateGroupAction] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
