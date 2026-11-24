from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt


class BatchUpdatePolicy(BaseModel):
    terminateJobsOnUpdate: StrictBool | None = None
    jobExecutionTimeoutMinutes: StrictInt | None = None
