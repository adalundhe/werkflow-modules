from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchServerlessBatchGetCollectionRequest(BaseModel):
    ids: list[StrictStr] | None = None
    names: list[StrictStr] | None = None
