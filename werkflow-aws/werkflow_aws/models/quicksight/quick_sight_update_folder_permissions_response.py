from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_resource_permission import QuickSightResourcePermission


class QuickSightUpdateFolderPermissionsResponse(BaseModel):
    Status: StrictInt | None = None
    Arn: StrictStr | None = None
    FolderId: StrictStr | None = None
    Permissions: list[QuickSightResourcePermission] | None = None
    RequestId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
