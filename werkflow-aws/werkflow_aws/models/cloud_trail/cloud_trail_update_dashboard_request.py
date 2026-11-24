from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .cloud_trail_refresh_schedule import CloudTrailRefreshSchedule
from .cloud_trail_request_widget import CloudTrailRequestWidget


class CloudTrailUpdateDashboardRequest(BaseModel):
    DashboardId: StrictStr
    Widgets: list[CloudTrailRequestWidget] | None = None
    RefreshSchedule: CloudTrailRefreshSchedule | None = None
    TerminationProtectionEnabled: StrictBool | None = None
