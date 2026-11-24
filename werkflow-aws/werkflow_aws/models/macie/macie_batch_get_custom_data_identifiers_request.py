from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MacieBatchGetCustomDataIdentifiersRequest(BaseModel):
    ids: list[StrictStr] | None = None
