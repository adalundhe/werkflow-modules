from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .quick_sight_space_contributor import QuickSightSpaceContributor
from .quick_sight_space_details import QuickSightSpaceDetails


class QuickSightDescribeSpaceResponse(BaseModel):
    spaceId: StrictStr | None = None
    spaceArn: StrictStr | None = None
    Space: QuickSightSpaceDetails | None = None
    Contributors: list[QuickSightSpaceContributor] | None = None
    RequestId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
