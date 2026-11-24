from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueDeletePartitionRequest(BaseModel):
    DatabaseName: StrictStr
    TableName: StrictStr
    PartitionValues: list[StrictStr]
    CatalogId: StrictStr | None = None
