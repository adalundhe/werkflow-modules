from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ECSUlimit(BaseModel):
    name: StrictStr | None = None
    softLimit: StrictInt | None = None
    hardLimit: StrictInt | None = None
