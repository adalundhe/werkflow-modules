from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StepFunctionsCloudWatchLogsLogGroup(BaseModel):
    logGroupArn: StrictStr | None = None
