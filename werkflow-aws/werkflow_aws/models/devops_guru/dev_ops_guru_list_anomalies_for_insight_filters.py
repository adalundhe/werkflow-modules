from __future__ import annotations
from pydantic import BaseModel
from .dev_ops_guru_service_collection import DevOpsGuruServiceCollection


class DevOpsGuruListAnomaliesForInsightFilters(BaseModel):
    ServiceCollection: DevOpsGuruServiceCollection | None = None
