from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_space_resource_operation import QuickSightSpaceResourceOperation


class QuickSightUpdateSpaceResourcesRequest(BaseModel):
    AwsAccountId: StrictStr
    SpaceId: StrictStr
    AddResources: list[QuickSightSpaceResourceOperation] | None = None
    RemoveResources: list[QuickSightSpaceResourceOperation] | None = None
