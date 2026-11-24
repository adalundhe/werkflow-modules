from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DataZoneEnvironmentSummary(BaseModel):
    projectId: StrictStr | None = None
    id: StrictStr | None = None
    domainId: StrictStr | None = None
    createdBy: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    name: StrictStr | None = None
    description: StrictStr | None = None
    environmentProfileId: StrictStr | None = None
    awsAccountId: StrictStr | None = None
    awsAccountRegion: StrictStr | None = None
    provider: StrictStr | None = None
    status: StrictStr | None = None
    environmentConfigurationId: StrictStr | None = None
    environmentConfigurationName: StrictStr | None = None
