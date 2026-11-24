from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .get_permission_holder_response import GetPermissionHolderResponse


class GetPermissionResponse(BaseModel):
    holder: GetPermissionHolderResponse | None = None
    type: StrictStr | None = None
