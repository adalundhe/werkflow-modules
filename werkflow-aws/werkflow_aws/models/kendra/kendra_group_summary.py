from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class KendraGroupSummary(BaseModel):
    GroupId: StrictStr | None = None
    OrderingId: StrictInt | None = None
