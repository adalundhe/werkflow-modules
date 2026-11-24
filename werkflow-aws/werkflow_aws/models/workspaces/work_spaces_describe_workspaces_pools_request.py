from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .work_spaces_describe_workspaces_pools_filter import WorkSpacesDescribeWorkspacesPoolsFilter


class WorkSpacesDescribeWorkspacesPoolsRequest(BaseModel):
    PoolIds: list[StrictStr] | None = None
    Filters: list[WorkSpacesDescribeWorkspacesPoolsFilter] | None = None
    Limit: StrictInt | None = None
    NextToken: StrictStr | None = None
