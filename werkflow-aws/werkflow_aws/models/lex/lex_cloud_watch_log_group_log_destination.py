from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexCloudWatchLogGroupLogDestination(BaseModel):
    cloudWatchLogGroupArn: StrictStr | None = None
    logPrefix: StrictStr | None = None
