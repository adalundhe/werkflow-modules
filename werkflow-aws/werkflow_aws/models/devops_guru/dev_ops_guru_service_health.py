from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .dev_ops_guru_service_insight_health import DevOpsGuruServiceInsightHealth


class DevOpsGuruServiceHealth(BaseModel):
    ServiceName: StrictStr | None = None
    Insight: DevOpsGuruServiceInsightHealth | None = None
    AnalyzedResourceCount: StrictInt | None = None
