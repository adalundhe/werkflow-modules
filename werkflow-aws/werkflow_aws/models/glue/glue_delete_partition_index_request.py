from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueDeletePartitionIndexRequest(BaseModel):
    DatabaseName: StrictStr
    TableName: StrictStr
    IndexName: StrictStr
    CatalogId: StrictStr | None = None
