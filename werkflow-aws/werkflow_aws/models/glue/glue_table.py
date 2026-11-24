from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueTable(BaseModel):
    DatabaseName: StrictStr | None = None
    TableName: StrictStr | None = None
    CatalogId: StrictStr | None = None
    ConnectionName: StrictStr | None = None
    AdditionalOptions: dict[StrictStr, StrictStr] | None = None
