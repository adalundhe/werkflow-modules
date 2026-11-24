from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_hierarchy_group_summary import ConnectHierarchyGroupSummary


class ConnectListUserHierarchyGroupsResponse(BaseModel):
    UserHierarchyGroupSummaryList: list[ConnectHierarchyGroupSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
