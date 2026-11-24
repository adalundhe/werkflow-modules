from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FISExperimentTemplateCloudWatchLogsLogConfiguration(BaseModel):
    logGroupArn: StrictStr | None = None
