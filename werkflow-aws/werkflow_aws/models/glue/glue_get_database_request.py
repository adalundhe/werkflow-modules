from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueGetDatabaseRequest(BaseModel):
    Name: StrictStr
    CatalogId: StrictStr | None = None
