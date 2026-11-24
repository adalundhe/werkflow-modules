from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class KinesisAnalyticsDescribeApplicationVersionRequest(BaseModel):
    ApplicationName: StrictStr
    ApplicationVersionId: StrictInt
