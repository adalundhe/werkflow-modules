from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_watch_logs_open_search_resource_status import CloudWatchLogsOpenSearchResourceStatus


class CloudWatchLogsOpenSearchApplication(BaseModel):
    applicationEndpoint: StrictStr | None = None
    applicationArn: StrictStr | None = None
    applicationId: StrictStr | None = None
    status: CloudWatchLogsOpenSearchResourceStatus | None = None
