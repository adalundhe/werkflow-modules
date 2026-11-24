from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class ResilienceHubAppVersionSummary(BaseModel):
    appVersion: StrictStr | None = None
    creationTime: datetime.datetime | StrictStr | None = None
    identifier: StrictInt | None = None
    versionName: StrictStr | None = None
