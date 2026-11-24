from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ResilienceHubStartMetricsExportRequest(BaseModel):
    bucketName: StrictStr | None = None
    clientToken: StrictStr | None = None
