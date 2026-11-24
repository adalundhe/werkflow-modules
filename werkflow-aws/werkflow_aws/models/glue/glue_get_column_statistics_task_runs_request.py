from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GlueGetColumnStatisticsTaskRunsRequest(BaseModel):
    DatabaseName: StrictStr
    TableName: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    CatalogID: StrictStr | None = None
