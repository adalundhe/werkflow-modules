from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchStorageTypeLimit(BaseModel):
    LimitName: StrictStr | None = None
    LimitValues: list[StrictStr] | None = None
