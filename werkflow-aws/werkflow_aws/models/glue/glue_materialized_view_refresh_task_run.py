from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class GlueMaterializedViewRefreshTaskRun(BaseModel):
    CustomerId: StrictStr | None = None
    MaterializedViewRefreshTaskRunId: StrictStr | None = None
    DatabaseName: StrictStr | None = None
    TableName: StrictStr | None = None
    CatalogId: StrictStr | None = None
    Role: StrictStr | None = None
    Status: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastUpdated: datetime.datetime | StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    ErrorMessage: StrictStr | None = None
    DPUSeconds: StrictFloat | StrictInt | None = None
    RefreshType: StrictStr | None = None
    ProcessedBytes: StrictInt | None = None
