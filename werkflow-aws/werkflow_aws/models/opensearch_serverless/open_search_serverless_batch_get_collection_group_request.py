from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchServerlessBatchGetCollectionGroupRequest(BaseModel):
    ids: list[StrictStr] | None = None
    names: list[StrictStr] | None = None
