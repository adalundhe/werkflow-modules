from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class WorkSpacesDescribeWorkspacesRequest(BaseModel):
    WorkspaceIds: list[StrictStr] | None = None
    DirectoryId: StrictStr | None = None
    UserName: StrictStr | None = None
    BundleId: StrictStr | None = None
    Limit: StrictInt | None = None
    NextToken: StrictStr | None = None
    WorkspaceName: StrictStr | None = None
