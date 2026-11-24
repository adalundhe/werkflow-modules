from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class OpenSearchDuration(BaseModel):
    Value: StrictInt | None = None
    Unit: StrictStr | None = None
