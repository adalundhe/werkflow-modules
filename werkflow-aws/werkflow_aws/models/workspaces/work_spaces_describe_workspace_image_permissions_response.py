from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .work_spaces_image_permission import WorkSpacesImagePermission


class WorkSpacesDescribeWorkspaceImagePermissionsResponse(BaseModel):
    ImageId: StrictStr | None = None
    ImagePermissions: list[WorkSpacesImagePermission] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
