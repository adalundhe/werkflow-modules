from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueDeleteTableRequest(BaseModel):
    DatabaseName: StrictStr
    Name: StrictStr
    CatalogId: StrictStr | None = None
    TransactionId: StrictStr | None = None
