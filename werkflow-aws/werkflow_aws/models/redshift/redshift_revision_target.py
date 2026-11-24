from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class RedshiftRevisionTarget(BaseModel):
    DatabaseRevision: StrictStr | None = None
    Description: StrictStr | None = None
    DatabaseRevisionReleaseDate: datetime.datetime | StrictStr | None = None
