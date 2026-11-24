from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DataZoneEnvironmentProfileSummary(BaseModel):
    id: StrictStr | None = None
    domainId: StrictStr | None = None
    awsAccountId: StrictStr | None = None
    awsAccountRegion: StrictStr | None = None
    createdBy: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    name: StrictStr | None = None
    description: StrictStr | None = None
    environmentBlueprintId: StrictStr | None = None
    projectId: StrictStr | None = None
