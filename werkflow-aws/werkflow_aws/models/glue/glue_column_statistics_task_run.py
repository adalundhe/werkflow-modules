from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class GlueColumnStatisticsTaskRun(BaseModel):
    CustomerId: StrictStr | None = None
    ColumnStatisticsTaskRunId: StrictStr | None = None
    DatabaseName: StrictStr | None = None
    TableName: StrictStr | None = None
    ColumnNameList: list[StrictStr] | None = None
    CatalogID: StrictStr | None = None
    Role: StrictStr | None = None
    SampleSize: StrictFloat | StrictInt | None = None
    SecurityConfiguration: StrictStr | None = None
    NumberOfWorkers: StrictInt | None = None
    WorkerType: StrictStr | None = None
    ComputationType: StrictStr | None = None
    Status: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastUpdated: datetime.datetime | StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    ErrorMessage: StrictStr | None = None
    DPUSeconds: StrictFloat | StrictInt | None = None
