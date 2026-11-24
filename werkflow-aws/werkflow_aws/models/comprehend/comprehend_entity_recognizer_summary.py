from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class ComprehendEntityRecognizerSummary(BaseModel):
    RecognizerName: StrictStr | None = None
    NumberOfVersions: StrictInt | None = None
    LatestVersionCreatedAt: datetime.datetime | StrictStr | None = None
    LatestVersionName: StrictStr | None = None
    LatestVersionStatus: StrictStr | None = None
