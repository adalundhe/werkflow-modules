from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataPipelineReportTaskRunnerHeartbeatRequest(BaseModel):
    taskrunnerId: StrictStr
    workerGroup: StrictStr | None = None
    hostname: StrictStr | None = None
