from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DevOpsGuruLogsAnomalyDetectionIntegration(BaseModel):
    OptInStatus: StrictStr | None = None
