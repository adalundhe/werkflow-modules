from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StatusMapping(BaseModel):
    issueTypeId: StrictStr | None = None
    newStatusId: StrictStr | None = None
    statusId: StrictStr | None = None
