from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictStr


class RestrictedPermission(BaseModel):
    model_config = ConfigDict(extra="allow")

    id: StrictStr | None = None
    key: StrictStr | None = None
