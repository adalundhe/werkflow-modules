from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GlueListColumnStatisticsTaskRunsRequest(BaseModel):
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
