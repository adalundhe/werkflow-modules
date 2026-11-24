from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_space_quick_sight_resource_details import QuickSightSpaceQuickSightResourceDetails


class QuickSightSpaceQuickSightResource(BaseModel):
    resourceType: StrictStr | None = None
    resourceDetails: QuickSightSpaceQuickSightResourceDetails | None = None
