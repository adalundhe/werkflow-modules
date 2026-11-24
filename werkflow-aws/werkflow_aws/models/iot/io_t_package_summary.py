from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class IoTPackageSummary(BaseModel):
    packageName: StrictStr | None = None
    defaultVersionName: StrictStr | None = None
    creationDate: datetime.datetime | StrictStr | None = None
    lastModifiedDate: datetime.datetime | StrictStr | None = None
