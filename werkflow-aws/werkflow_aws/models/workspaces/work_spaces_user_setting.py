from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class WorkSpacesUserSetting(BaseModel):
    Action: StrictStr | None = None
    Permission: StrictStr | None = None
    MaximumLength: StrictInt | None = None
