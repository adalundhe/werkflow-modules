from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .resilience_hub_event_subscription import ResilienceHubEventSubscription
from .resilience_hub_permission_model import ResilienceHubPermissionModel


class ResilienceHubCreateAppRequest(BaseModel):
    name: StrictStr
    assessmentSchedule: Literal['Disabled', 'Daily'] | None = None
    awsApplicationArn: StrictStr | None = None
    clientToken: StrictStr | None = None
    description: StrictStr | None = None
    eventSubscriptions: list[ResilienceHubEventSubscription] | None = None
    permissionModel: ResilienceHubPermissionModel | None = None
    policyArn: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
