from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .cloud_trail_refresh_schedule import CloudTrailRefreshSchedule
from .cloud_trail_widget import CloudTrailWidget


class CloudTrailGetDashboardResponse(BaseModel):
    DashboardArn: StrictStr | None = None
    Type: StrictStr | None = None
    Status: StrictStr | None = None
    Widgets: list[CloudTrailWidget] | None = None
    RefreshSchedule: CloudTrailRefreshSchedule | None = None
    CreatedTimestamp: datetime.datetime | StrictStr | None = None
    UpdatedTimestamp: datetime.datetime | StrictStr | None = None
    LastRefreshId: StrictStr | None = None
    LastRefreshFailureReason: StrictStr | None = None
    TerminationProtectionEnabled: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
