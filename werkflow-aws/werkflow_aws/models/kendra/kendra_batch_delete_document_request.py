from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kendra_data_source_sync_job_metric_target import KendraDataSourceSyncJobMetricTarget


class KendraBatchDeleteDocumentRequest(BaseModel):
    IndexId: StrictStr
    DocumentIdList: list[StrictStr]
    DataSourceSyncJobMetricTarget: KendraDataSourceSyncJobMetricTarget | None = None
