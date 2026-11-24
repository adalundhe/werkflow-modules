from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr


class UserPermission(BaseModel):
    model_config = ConfigDict(extra="allow")

    deprecatedKey: StrictBool | None = None
    description: StrictStr | None = None
    havePermission: StrictBool | None = None
    id: StrictStr | None = None
    key: StrictStr | None = None
    name: StrictStr | None = None
    type: StrictStr | None = None
