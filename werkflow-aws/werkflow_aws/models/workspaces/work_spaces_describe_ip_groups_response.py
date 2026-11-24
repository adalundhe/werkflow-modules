from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .workspaces_ip_group import WorkspacesIpGroup


class WorkSpacesDescribeIpGroupsResponse(BaseModel):
    Result: list[WorkspacesIpGroup] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
