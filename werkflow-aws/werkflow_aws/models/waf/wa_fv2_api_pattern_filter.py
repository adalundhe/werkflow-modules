from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class WAFv2ApiPatternFilter(BaseModel):
    Method: StrictStr | None = None
    PathPattern: StrictStr | None = None
    Port: StrictInt | None = None
    Domains: list[StrictStr] | None = None
