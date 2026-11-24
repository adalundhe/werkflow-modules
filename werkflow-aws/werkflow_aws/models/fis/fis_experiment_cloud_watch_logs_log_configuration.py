from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FISExperimentCloudWatchLogsLogConfiguration(BaseModel):
    logGroupArn: StrictStr | None = None
