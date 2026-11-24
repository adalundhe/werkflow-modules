from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .dev_ops_guru_event_resource import DevOpsGuruEventResource
from .dev_ops_guru_resource_collection import DevOpsGuruResourceCollection


class DevOpsGuruEvent(BaseModel):
    ResourceCollection: DevOpsGuruResourceCollection | None = None
    Id: StrictStr | None = None
    Time: datetime.datetime | StrictStr | None = None
    EventSource: StrictStr | None = None
    Name: StrictStr | None = None
    DataSource: StrictStr | None = None
    EventClass: StrictStr | None = None
    Resources: list[DevOpsGuruEventResource] | None = None
