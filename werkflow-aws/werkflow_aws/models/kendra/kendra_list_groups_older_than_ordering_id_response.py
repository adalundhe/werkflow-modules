from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .kendra_group_summary import KendraGroupSummary


class KendraListGroupsOlderThanOrderingIdResponse(BaseModel):
    GroupsSummaries: list[KendraGroupSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
