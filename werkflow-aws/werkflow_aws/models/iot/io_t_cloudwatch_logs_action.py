from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class IoTCloudwatchLogsAction(BaseModel):
    roleArn: StrictStr | None = None
    logGroupName: StrictStr | None = None
    batchMode: StrictBool | None = None
