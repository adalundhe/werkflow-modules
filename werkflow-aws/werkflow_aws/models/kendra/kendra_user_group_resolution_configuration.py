from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraUserGroupResolutionConfiguration(BaseModel):
    UserGroupResolutionMode: StrictStr | None = None
