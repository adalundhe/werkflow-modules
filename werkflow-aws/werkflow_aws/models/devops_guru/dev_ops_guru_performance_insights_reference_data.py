from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dev_ops_guru_performance_insights_reference_comparison_values import DevOpsGuruPerformanceInsightsReferenceComparisonValues


class DevOpsGuruPerformanceInsightsReferenceData(BaseModel):
    Name: StrictStr | None = None
    ComparisonValues: DevOpsGuruPerformanceInsightsReferenceComparisonValues | None = None
