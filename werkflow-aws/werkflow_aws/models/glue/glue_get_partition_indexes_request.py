from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueGetPartitionIndexesRequest(BaseModel):
    DatabaseName: StrictStr
    TableName: StrictStr
    CatalogId: StrictStr | None = None
    NextToken: StrictStr | None = None
