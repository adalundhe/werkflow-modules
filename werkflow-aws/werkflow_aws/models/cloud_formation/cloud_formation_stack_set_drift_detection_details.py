from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class CloudFormationStackSetDriftDetectionDetails(BaseModel):
    DriftStatus: StrictStr | None = None
    DriftDetectionStatus: StrictStr | None = None
    LastDriftCheckTimestamp: datetime.datetime | StrictStr | None = None
    TotalStackInstancesCount: StrictInt | None = None
    DriftedStackInstancesCount: StrictInt | None = None
    InSyncStackInstancesCount: StrictInt | None = None
    InProgressStackInstancesCount: StrictInt | None = None
    FailedStackInstancesCount: StrictInt | None = None
