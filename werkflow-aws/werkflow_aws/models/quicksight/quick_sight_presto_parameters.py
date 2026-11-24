from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightPrestoParameters(BaseModel):
    Host: StrictStr | None = None
    Port: StrictInt | None = None
    Catalog: StrictStr | None = None
