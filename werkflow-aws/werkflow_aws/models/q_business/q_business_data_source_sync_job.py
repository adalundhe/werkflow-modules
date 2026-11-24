from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .q_business_data_source_sync_job_metrics import QBusinessDataSourceSyncJobMetrics
from .q_business_error_detail import QBusinessErrorDetail


class QBusinessDataSourceSyncJob(BaseModel):
    executionId: StrictStr | None = None
    startTime: datetime.datetime | StrictStr | None = None
    endTime: datetime.datetime | StrictStr | None = None
    status: StrictStr | None = None
    error: QBusinessErrorDetail | None = None
    dataSourceErrorCode: StrictStr | None = None
    metrics: QBusinessDataSourceSyncJobMetrics | None = None
