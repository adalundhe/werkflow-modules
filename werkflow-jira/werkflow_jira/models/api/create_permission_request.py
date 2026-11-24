from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .create_permission_holder_request import CreatePermissionHolderRequest


class CreatePermissionRequest(BaseModel):
    holder: CreatePermissionHolderRequest | None = None
    type: StrictStr | None = None
