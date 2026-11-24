from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class Error(BaseModel):
    count: StrictInt | None = None
    issueIdsOrKeys: list[StrictStr] | None = None
    message: StrictStr | None = None
