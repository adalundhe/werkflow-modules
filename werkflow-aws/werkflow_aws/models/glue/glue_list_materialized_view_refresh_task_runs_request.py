from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GlueListMaterializedViewRefreshTaskRunsRequest(BaseModel):
    CatalogId: StrictStr
    DatabaseName: StrictStr | None = None
    TableName: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
