from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PermissionHolder(BaseModel):
    expand: StrictStr | None = None
    parameter: StrictStr | None = None
    type: StrictStr | None = None
    value: StrictStr | None = None
