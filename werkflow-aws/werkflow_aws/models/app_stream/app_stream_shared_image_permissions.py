from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_stream_image_permissions import AppStreamImagePermissions


class AppStreamSharedImagePermissions(BaseModel):
    sharedAccountId: StrictStr | None = None
    imagePermissions: AppStreamImagePermissions | None = None
