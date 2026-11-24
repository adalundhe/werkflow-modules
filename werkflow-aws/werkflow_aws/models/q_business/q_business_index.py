from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class QBusinessIndex(BaseModel):
    displayName: StrictStr | None = None
    indexId: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    status: StrictStr | None = None
