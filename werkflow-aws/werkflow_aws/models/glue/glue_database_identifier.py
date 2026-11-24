from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueDatabaseIdentifier(BaseModel):
    CatalogId: StrictStr | None = None
    DatabaseName: StrictStr | None = None
    Region: StrictStr | None = None
