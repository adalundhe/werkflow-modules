from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_stream_image_permissions import AppStreamImagePermissions


class AppStreamUpdateImagePermissionsRequest(BaseModel):
    Name: StrictStr
    SharedAccountId: StrictStr
    ImagePermissions: AppStreamImagePermissions
