from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CreatePermissionHolderRequest(BaseModel):
    type: StrictStr | None = None
    value: StrictStr | None = None
