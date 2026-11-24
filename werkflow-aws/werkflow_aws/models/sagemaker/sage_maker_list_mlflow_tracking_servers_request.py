from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerListMlflowTrackingServersRequest(BaseModel):
    CreatedAfter: datetime.datetime | StrictStr | None = None
    CreatedBefore: datetime.datetime | StrictStr | None = None
    TrackingServerStatus: Literal['Creating', 'Created', 'CreateFailed', 'Updating', 'Updated', 'UpdateFailed', 'Deleting', 'DeleteFailed', 'Stopping', 'Stopped', 'StopFailed', 'Starting', 'Started', 'StartFailed', 'MaintenanceInProgress', 'MaintenanceComplete', 'MaintenanceFailed'] | None = None
    MlflowVersion: StrictStr | None = None
    SortBy: Literal['Name', 'CreationTime', 'Status'] | None = None
    SortOrder: Literal['Ascending', 'Descending'] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
