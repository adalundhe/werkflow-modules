from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SearchWarningLimitDetails(BaseModel):
    actual: StrictInt | None = None
    arguments: StrictStr | None = None
    clause: StrictStr | None = None
    limit: StrictInt | None = None
