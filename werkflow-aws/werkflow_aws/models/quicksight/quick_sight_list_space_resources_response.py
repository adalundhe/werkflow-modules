from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .quick_sight_space_resource_summary import QuickSightSpaceResourceSummary


class QuickSightListSpaceResourcesResponse(BaseModel):
    spaceId: StrictStr | None = None
    spaceArn: StrictStr | None = None
    SpaceResources: list[QuickSightSpaceResourceSummary] | None = None
    RequestId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
