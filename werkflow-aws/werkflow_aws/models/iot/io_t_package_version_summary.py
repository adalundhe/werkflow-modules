from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class IoTPackageVersionSummary(BaseModel):
    packageName: StrictStr | None = None
    versionName: StrictStr | None = None
    status: StrictStr | None = None
    creationDate: datetime.datetime | StrictStr | None = None
    lastModifiedDate: datetime.datetime | StrictStr | None = None
