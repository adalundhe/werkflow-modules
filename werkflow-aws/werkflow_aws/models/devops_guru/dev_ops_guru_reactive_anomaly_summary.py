from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dev_ops_guru_anomaly_reported_time_range import DevOpsGuruAnomalyReportedTimeRange
from .dev_ops_guru_anomaly_resource import DevOpsGuruAnomalyResource
from .dev_ops_guru_anomaly_source_details import DevOpsGuruAnomalySourceDetails
from .dev_ops_guru_anomaly_time_range import DevOpsGuruAnomalyTimeRange
from .dev_ops_guru_resource_collection import DevOpsGuruResourceCollection


class DevOpsGuruReactiveAnomalySummary(BaseModel):
    Id: StrictStr | None = None
    Severity: StrictStr | None = None
    Status: StrictStr | None = None
    AnomalyTimeRange: DevOpsGuruAnomalyTimeRange | None = None
    AnomalyReportedTimeRange: DevOpsGuruAnomalyReportedTimeRange | None = None
    SourceDetails: DevOpsGuruAnomalySourceDetails | None = None
    AssociatedInsightId: StrictStr | None = None
    ResourceCollection: DevOpsGuruResourceCollection | None = None
    Type: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    CausalAnomalyId: StrictStr | None = None
    AnomalyResources: list[DevOpsGuruAnomalyResource] | None = None
