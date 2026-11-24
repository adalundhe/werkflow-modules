from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueDeleteConnectionRequest(BaseModel):
    ConnectionName: StrictStr
    CatalogId: StrictStr | None = None
