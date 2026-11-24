from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueDeleteTableVersionRequest(BaseModel):
    DatabaseName: StrictStr
    TableName: StrictStr
    VersionId: StrictStr
    CatalogId: StrictStr | None = None
