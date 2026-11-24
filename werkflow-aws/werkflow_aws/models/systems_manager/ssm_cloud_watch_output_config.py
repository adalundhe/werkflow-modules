from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SSMCloudWatchOutputConfig(BaseModel):
    CloudWatchLogGroupName: StrictStr | None = None
    CloudWatchOutputEnabled: StrictBool | None = None
