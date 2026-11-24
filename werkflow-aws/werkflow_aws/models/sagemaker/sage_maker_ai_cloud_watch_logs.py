from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerAICloudWatchLogs(BaseModel):
    LogGroupArn: StrictStr | None = None
    LogStreamName: StrictStr | None = None
