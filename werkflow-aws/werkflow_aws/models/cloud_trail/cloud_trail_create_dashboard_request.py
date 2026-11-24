from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .cloud_trail_refresh_schedule import CloudTrailRefreshSchedule
from .cloud_trail_request_widget import CloudTrailRequestWidget
from .cloud_trail_tag import CloudTrailTag


class CloudTrailCreateDashboardRequest(BaseModel):
    Name: StrictStr
    RefreshSchedule: CloudTrailRefreshSchedule | None = None
    TagsList: list[CloudTrailTag] | None = None
    TerminationProtectionEnabled: StrictBool | None = None
    Widgets: list[CloudTrailRequestWidget] | None = None
