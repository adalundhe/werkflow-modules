from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_watch_logs_data_source import CloudWatchLogsDataSource


class CloudWatchLogsAssociateSourceToS3TableIntegrationRequest(BaseModel):
    integrationArn: StrictStr
    dataSource: CloudWatchLogsDataSource
