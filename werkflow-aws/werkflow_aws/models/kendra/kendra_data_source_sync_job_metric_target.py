from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraDataSourceSyncJobMetricTarget(BaseModel):
    DataSourceId: StrictStr
    DataSourceSyncJobId: StrictStr | None = None
