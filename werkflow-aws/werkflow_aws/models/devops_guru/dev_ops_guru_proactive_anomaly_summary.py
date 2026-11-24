from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .dev_ops_guru_anomaly_reported_time_range import DevOpsGuruAnomalyReportedTimeRange
from .dev_ops_guru_anomaly_resource import DevOpsGuruAnomalyResource
from .dev_ops_guru_anomaly_source_details import DevOpsGuruAnomalySourceDetails
from .dev_ops_guru_anomaly_source_metadata import DevOpsGuruAnomalySourceMetadata
from .dev_ops_guru_anomaly_time_range import DevOpsGuruAnomalyTimeRange
from .dev_ops_guru_prediction_time_range import DevOpsGuruPredictionTimeRange
from .dev_ops_guru_resource_collection import DevOpsGuruResourceCollection


class DevOpsGuruProactiveAnomalySummary(BaseModel):
    Id: StrictStr | None = None
    Severity: StrictStr | None = None
    Status: StrictStr | None = None
    UpdateTime: datetime.datetime | StrictStr | None = None
    AnomalyTimeRange: DevOpsGuruAnomalyTimeRange | None = None
    AnomalyReportedTimeRange: DevOpsGuruAnomalyReportedTimeRange | None = None
    PredictionTimeRange: DevOpsGuruPredictionTimeRange | None = None
    SourceDetails: DevOpsGuruAnomalySourceDetails | None = None
    AssociatedInsightId: StrictStr | None = None
    ResourceCollection: DevOpsGuruResourceCollection | None = None
    Limit: StrictFloat | StrictInt | None = None
    SourceMetadata: DevOpsGuruAnomalySourceMetadata | None = None
    AnomalyResources: list[DevOpsGuruAnomalyResource] | None = None
    Description: StrictStr | None = None
