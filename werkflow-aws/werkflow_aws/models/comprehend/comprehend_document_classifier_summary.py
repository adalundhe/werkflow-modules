from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class ComprehendDocumentClassifierSummary(BaseModel):
    DocumentClassifierName: StrictStr | None = None
    NumberOfVersions: StrictInt | None = None
    LatestVersionCreatedAt: datetime.datetime | StrictStr | None = None
    LatestVersionName: StrictStr | None = None
    LatestVersionStatus: StrictStr | None = None
