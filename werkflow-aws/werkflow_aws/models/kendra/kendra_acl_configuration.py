from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraAclConfiguration(BaseModel):
    AllowedGroupsColumnName: StrictStr | None = None
