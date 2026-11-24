from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class MacieCustomDataIdentifierSummary(BaseModel):
    arn: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    description: StrictStr | None = None
    id: StrictStr | None = None
    name: StrictStr | None = None
