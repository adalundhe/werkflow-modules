from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class WorkSpacesDescribeWorkspaceImagePermissionsRequest(BaseModel):
    ImageId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
