from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_watch_logs_open_search_resource_status import CloudWatchLogsOpenSearchResourceStatus


class CloudWatchLogsOpenSearchNetworkPolicy(BaseModel):
    policyName: StrictStr | None = None
    status: CloudWatchLogsOpenSearchResourceStatus | None = None
