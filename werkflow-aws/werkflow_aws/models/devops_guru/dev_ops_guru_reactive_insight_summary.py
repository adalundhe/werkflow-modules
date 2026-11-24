from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dev_ops_guru_insight_time_range import DevOpsGuruInsightTimeRange
from .dev_ops_guru_resource_collection import DevOpsGuruResourceCollection
from .dev_ops_guru_service_collection import DevOpsGuruServiceCollection


class DevOpsGuruReactiveInsightSummary(BaseModel):
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    Severity: StrictStr | None = None
    Status: StrictStr | None = None
    InsightTimeRange: DevOpsGuruInsightTimeRange | None = None
    ResourceCollection: DevOpsGuruResourceCollection | None = None
    ServiceCollection: DevOpsGuruServiceCollection | None = None
    AssociatedResourceArns: list[StrictStr] | None = None
