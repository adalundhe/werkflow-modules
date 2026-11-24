from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .q_business_group_summary import QBusinessGroupSummary


class QBusinessListGroupsResponse(BaseModel):
    nextToken: StrictStr | None = None
    items: list[QBusinessGroupSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
