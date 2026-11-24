from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchGetMetricDataQueryDefinitionRequest(BaseModel):
    Id: StrictStr
