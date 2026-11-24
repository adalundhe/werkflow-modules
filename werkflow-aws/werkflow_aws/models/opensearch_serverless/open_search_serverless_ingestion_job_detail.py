from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .open_search_serverless_ingestion_alert import OpenSearchServerlessIngestionAlert
from .open_search_serverless_ingestion_failure_reason import OpenSearchServerlessIngestionFailureReason
from .open_search_serverless_ingestion_job_source import OpenSearchServerlessIngestionJobSource
from .open_search_serverless_ingestion_statistics import OpenSearchServerlessIngestionStatistics


class OpenSearchServerlessIngestionJobDetail(BaseModel):
    ingestionJobId: StrictStr | None = None
    arn: StrictStr | None = None
    collectionId: StrictStr | None = None
    ingestionJobName: StrictStr | None = None
    indexName: StrictStr | None = None
    failureIndexName: StrictStr | None = None
    source: OpenSearchServerlessIngestionJobSource | None = None
    status: StrictStr | None = None
    state: StrictStr | None = None
    statistics: OpenSearchServerlessIngestionStatistics | None = None
    revision: StrictInt | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    failureReasons: list[OpenSearchServerlessIngestionFailureReason] | None = None
    activeAlerts: list[OpenSearchServerlessIngestionAlert] | None = None
