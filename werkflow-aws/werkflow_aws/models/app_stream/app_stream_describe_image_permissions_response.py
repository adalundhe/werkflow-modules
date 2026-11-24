from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .app_stream_shared_image_permissions import AppStreamSharedImagePermissions


class AppStreamDescribeImagePermissionsResponse(BaseModel):
    Name: StrictStr | None = None
    SharedImagePermissionsList: list[AppStreamSharedImagePermissions] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
