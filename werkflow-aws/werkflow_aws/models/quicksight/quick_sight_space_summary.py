from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightSpaceSummary(BaseModel):
    spaceId: StrictStr | None = None
    spaceArn: StrictStr | None = None
    name: StrictStr | None = None
    description: StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    consumedSourceSize: StrictInt | None = None
    consumedSourceDocCount: StrictInt | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    createdBy: StrictStr | None = None
    createdByArn: StrictStr | None = None
    resourcesCount: StrictInt | None = None
