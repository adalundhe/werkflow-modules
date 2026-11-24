from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchAdditionalLimit(BaseModel):
    LimitName: StrictStr | None = None
    LimitValues: list[StrictStr] | None = None
