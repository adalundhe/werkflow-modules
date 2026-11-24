from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppSyncEnhancedMetricsConfig(BaseModel):
    resolverLevelMetricsBehavior: StrictStr | None = None
    dataSourceLevelMetricsBehavior: StrictStr | None = None
    operationLevelMetricsConfig: StrictStr | None = None
