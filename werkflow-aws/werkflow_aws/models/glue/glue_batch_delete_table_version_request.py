from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueBatchDeleteTableVersionRequest(BaseModel):
    DatabaseName: StrictStr
    TableName: StrictStr
    VersionIds: list[StrictStr]
    CatalogId: StrictStr | None = None
