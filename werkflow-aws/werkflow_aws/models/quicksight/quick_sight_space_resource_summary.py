from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .quick_sight_space_quick_sight_resource_details import QuickSightSpaceQuickSightResourceDetails


class QuickSightSpaceResourceSummary(BaseModel):
    ResourceType: StrictStr | None = None
    ResourceDetails: QuickSightSpaceQuickSightResourceDetails | None = None
    ResourceName: StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
