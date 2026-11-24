from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MacieListManagedDataIdentifiersRequest(BaseModel):
    nextToken: StrictStr | None = None
