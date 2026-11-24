from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class AppStreamResourceError(BaseModel):
    ErrorCode: StrictStr | None = None
    ErrorMessage: StrictStr | None = None
    ErrorTimestamp: datetime.datetime | StrictStr | None = None
