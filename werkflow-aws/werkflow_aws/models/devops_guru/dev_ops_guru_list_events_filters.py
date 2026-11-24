from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .dev_ops_guru_event_time_range import DevOpsGuruEventTimeRange
from .dev_ops_guru_resource_collection import DevOpsGuruResourceCollection


class DevOpsGuruListEventsFilters(BaseModel):
    InsightId: StrictStr | None = None
    EventTimeRange: DevOpsGuruEventTimeRange | None = None
    EventClass: Literal['INFRASTRUCTURE', 'DEPLOYMENT', 'SECURITY_CHANGE', 'CONFIG_CHANGE', 'SCHEMA_CHANGE'] | None = None
    EventSource: StrictStr | None = None
    DataSource: Literal['AWS_CLOUD_TRAIL', 'AWS_CODE_DEPLOY'] | None = None
    ResourceCollection: DevOpsGuruResourceCollection | None = None
