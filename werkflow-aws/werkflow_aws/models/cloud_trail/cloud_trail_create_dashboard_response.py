from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .cloud_trail_refresh_schedule import CloudTrailRefreshSchedule
from .cloud_trail_tag import CloudTrailTag
from .cloud_trail_widget import CloudTrailWidget


class CloudTrailCreateDashboardResponse(BaseModel):
    DashboardArn: StrictStr | None = None
    Name: StrictStr | None = None
    Type: StrictStr | None = None
    Widgets: list[CloudTrailWidget] | None = None
    TagsList: list[CloudTrailTag] | None = None
    RefreshSchedule: CloudTrailRefreshSchedule | None = None
    TerminationProtectionEnabled: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
