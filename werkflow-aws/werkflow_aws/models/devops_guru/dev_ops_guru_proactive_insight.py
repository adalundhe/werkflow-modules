from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dev_ops_guru_insight_time_range import DevOpsGuruInsightTimeRange
from .dev_ops_guru_prediction_time_range import DevOpsGuruPredictionTimeRange
from .dev_ops_guru_resource_collection import DevOpsGuruResourceCollection


class DevOpsGuruProactiveInsight(BaseModel):
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    Severity: StrictStr | None = None
    Status: StrictStr | None = None
    InsightTimeRange: DevOpsGuruInsightTimeRange | None = None
    PredictionTimeRange: DevOpsGuruPredictionTimeRange | None = None
    ResourceCollection: DevOpsGuruResourceCollection | None = None
    SsmOpsItemId: StrictStr | None = None
    Description: StrictStr | None = None
