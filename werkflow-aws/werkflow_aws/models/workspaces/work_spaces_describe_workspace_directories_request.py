from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .work_spaces_describe_workspace_directories_filter import WorkSpacesDescribeWorkspaceDirectoriesFilter


class WorkSpacesDescribeWorkspaceDirectoriesRequest(BaseModel):
    DirectoryIds: list[StrictStr] | None = None
    WorkspaceDirectoryNames: list[StrictStr] | None = None
    Limit: StrictInt | None = None
    NextToken: StrictStr | None = None
    Filters: list[WorkSpacesDescribeWorkspaceDirectoriesFilter] | None = None
