from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueBatchDeleteConnectionRequest(BaseModel):
    ConnectionNameList: list[StrictStr]
    CatalogId: StrictStr | None = None
