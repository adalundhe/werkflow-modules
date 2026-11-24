from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .auto_scaling_notification_configuration import AutoScalingNotificationConfiguration


class AutoScalingDescribeNotificationConfigurationsResponse(BaseModel):
    NotificationConfigurations: list[AutoScalingNotificationConfiguration] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
