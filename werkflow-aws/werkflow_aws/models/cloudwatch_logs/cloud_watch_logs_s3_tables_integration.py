from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsS3TablesIntegration(BaseModel):
    datasourceName: StrictStr | None = None
    datasourceType: StrictStr | None = None
