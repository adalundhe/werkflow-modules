from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .dev_ops_guru_list_monitored_resources_filters import DevOpsGuruListMonitoredResourcesFilters


class DevOpsGuruListMonitoredResourcesRequest(BaseModel):
    Filters: DevOpsGuruListMonitoredResourcesFilters | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
