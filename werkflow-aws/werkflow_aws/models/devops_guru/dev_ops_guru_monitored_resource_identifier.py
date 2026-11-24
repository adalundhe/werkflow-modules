from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .dev_ops_guru_resource_collection import DevOpsGuruResourceCollection


class DevOpsGuruMonitoredResourceIdentifier(BaseModel):
    MonitoredResourceName: StrictStr | None = None
    Type: StrictStr | None = None
    ResourcePermission: StrictStr | None = None
    LastUpdated: datetime.datetime | StrictStr | None = None
    ResourceCollection: DevOpsGuruResourceCollection | None = None
