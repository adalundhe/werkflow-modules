from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_space_quick_sight_resource import QuickSightSpaceQuickSightResource


class QuickSightSpaceDetails(BaseModel):
    name: StrictStr | None = None
    description: StrictStr | None = None
    resources: list[QuickSightSpaceQuickSightResource] | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    consumedSourceSize: StrictInt | None = None
    consumedSourceDocCount: StrictInt | None = None
    createdBy: StrictStr | None = None
    createdByArn: StrictStr | None = None
