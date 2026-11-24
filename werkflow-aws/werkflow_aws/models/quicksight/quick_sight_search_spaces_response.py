from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .quick_sight_space_summary import QuickSightSpaceSummary


class QuickSightSearchSpacesResponse(BaseModel):
    spaceId: StrictStr | None = None
    spaceArn: StrictStr | None = None
    SpaceSummaries: list[QuickSightSpaceSummary] | None = None
    NextToken: StrictStr | None = None
    RequestId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
