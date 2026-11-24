from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ssm_maintenance_window_filter import SSMMaintenanceWindowFilter


class SSMDescribeMaintenanceWindowExecutionsRequest(BaseModel):
    WindowId: StrictStr
    Filters: list[SSMMaintenanceWindowFilter] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
