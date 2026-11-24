from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class LakeFormationListTransactionsRequest(BaseModel):
    CatalogId: StrictStr | None = None
    StatusFilter: Literal['ALL', 'COMPLETED', 'ACTIVE', 'COMMITTED', 'ABORTED'] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
