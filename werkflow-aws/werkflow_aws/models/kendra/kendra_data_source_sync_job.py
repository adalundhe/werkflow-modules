from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .kendra_data_source_sync_job_metrics import KendraDataSourceSyncJobMetrics


class KendraDataSourceSyncJob(BaseModel):
    ExecutionId: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
    ErrorMessage: StrictStr | None = None
    ErrorCode: StrictStr | None = None
    DataSourceErrorCode: StrictStr | None = None
    Metrics: KendraDataSourceSyncJobMetrics | None = None
