from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .dev_ops_guru_insight_health import DevOpsGuruInsightHealth


class DevOpsGuruCloudFormationHealth(BaseModel):
    StackName: StrictStr | None = None
    Insight: DevOpsGuruInsightHealth | None = None
    AnalyzedResourceCount: StrictInt | None = None
