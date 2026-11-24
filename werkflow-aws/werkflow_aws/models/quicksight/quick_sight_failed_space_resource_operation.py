from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_space_quick_sight_resource_details import QuickSightSpaceQuickSightResourceDetails


class QuickSightFailedSpaceResourceOperation(BaseModel):
    ResourceType: StrictStr | None = None
    ResourceDetails: QuickSightSpaceQuickSightResourceDetails | None = None
    ErrorMessage: StrictStr | None = None
