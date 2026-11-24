from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class QBusinessDataSource(BaseModel):
    displayName: StrictStr | None = None
    dataSourceId: StrictStr | None = None
    type: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    status: StrictStr | None = None
