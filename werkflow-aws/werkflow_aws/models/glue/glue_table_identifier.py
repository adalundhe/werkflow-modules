from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueTableIdentifier(BaseModel):
    CatalogId: StrictStr | None = None
    DatabaseName: StrictStr | None = None
    Name: StrictStr | None = None
    Region: StrictStr | None = None
