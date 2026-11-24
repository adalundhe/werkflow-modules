from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class MacieAllowListSummary(BaseModel):
    arn: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    description: StrictStr | None = None
    id: StrictStr | None = None
    name: StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
