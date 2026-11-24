from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SecurityLakeDataLakeException(BaseModel):
    exception: StrictStr | None = None
    region: StrictStr | None = None
    remediation: StrictStr | None = None
    timestamp: datetime.datetime | StrictStr | None = None
