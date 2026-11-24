from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class LexImportSummary(BaseModel):
    importId: StrictStr | None = None
    importedResourceId: StrictStr | None = None
    importedResourceName: StrictStr | None = None
    importStatus: StrictStr | None = None
    mergeStrategy: StrictStr | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    lastUpdatedDateTime: datetime.datetime | StrictStr | None = None
    importedResourceType: StrictStr | None = None
