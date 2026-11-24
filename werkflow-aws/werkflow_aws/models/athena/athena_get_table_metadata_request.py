from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AthenaGetTableMetadataRequest(BaseModel):
    CatalogName: StrictStr
    DatabaseName: StrictStr
    TableName: StrictStr
    WorkGroup: StrictStr | None = None
