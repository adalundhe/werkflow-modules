from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueDeleteDatabaseRequest(BaseModel):
    Name: StrictStr
    CatalogId: StrictStr | None = None
