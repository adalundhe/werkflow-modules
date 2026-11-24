from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class MSKReplicatorCloudWatchLogs(BaseModel):
    Enabled: StrictBool | None = None
    LogGroup: StrictStr | None = None
