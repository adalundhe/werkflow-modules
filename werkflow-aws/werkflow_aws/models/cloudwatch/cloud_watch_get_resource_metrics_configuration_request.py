from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchGetResourceMetricsConfigurationRequest(BaseModel):
    ResourceArn: StrictStr
