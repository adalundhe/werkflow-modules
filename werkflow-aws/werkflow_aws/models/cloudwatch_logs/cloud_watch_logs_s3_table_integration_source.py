from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .cloud_watch_logs_data_source import CloudWatchLogsDataSource


class CloudWatchLogsS3TableIntegrationSource(BaseModel):
    identifier: StrictStr | None = None
    dataSource: CloudWatchLogsDataSource | None = None
    status: StrictStr | None = None
    statusReason: StrictStr | None = None
    createdTimeStamp: StrictInt | None = None
    parentSourceIdentifier: StrictStr | None = None
