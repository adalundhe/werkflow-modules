from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueBatchDeleteTableRequest(BaseModel):
    DatabaseName: StrictStr
    TablesToDelete: list[StrictStr]
    CatalogId: StrictStr | None = None
    TransactionId: StrictStr | None = None
