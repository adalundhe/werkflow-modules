from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .quick_sight_failed_space_resource_operation import QuickSightFailedSpaceResourceOperation


class QuickSightUpdateSpaceResourcesResponse(BaseModel):
    spaceId: StrictStr | None = None
    spaceArn: StrictStr | None = None
    FailedResourceOperations: list[QuickSightFailedSpaceResourceOperation] | None = None
    RequestId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
