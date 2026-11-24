from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dev_ops_guru_account_insight_health import DevOpsGuruAccountInsightHealth


class DevOpsGuruAccountHealth(BaseModel):
    AccountId: StrictStr | None = None
    Insight: DevOpsGuruAccountInsightHealth | None = None
