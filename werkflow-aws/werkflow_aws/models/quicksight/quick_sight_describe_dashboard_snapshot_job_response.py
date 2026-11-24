from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_snapshot_configuration import QuickSightSnapshotConfiguration
from .quick_sight_snapshot_user_configuration_redacted import QuickSightSnapshotUserConfigurationRedacted


class QuickSightDescribeDashboardSnapshotJobResponse(BaseModel):
    AwsAccountId: StrictStr | None = None
    DashboardId: StrictStr | None = None
    SnapshotJobId: StrictStr | None = None
    UserConfiguration: QuickSightSnapshotUserConfigurationRedacted | None = None
    SnapshotConfiguration: QuickSightSnapshotConfiguration | None = None
    Arn: StrictStr | None = None
    JobStatus: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
    RequestId: StrictStr | None = None
    Status: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
