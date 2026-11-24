from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsGetLogFieldsRequest(BaseModel):
    dataSourceName: StrictStr
    dataSourceType: StrictStr
