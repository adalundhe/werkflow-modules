from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MacieListClassificationScopesRequest(BaseModel):
    name: StrictStr | None = None
    nextToken: StrictStr | None = None
