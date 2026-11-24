from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class BatchUlimit(BaseModel):
    hardLimit: StrictInt | None = None
    name: StrictStr | None = None
    softLimit: StrictInt | None = None
