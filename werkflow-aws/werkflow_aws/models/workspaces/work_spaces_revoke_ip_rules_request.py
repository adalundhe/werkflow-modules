from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesRevokeIpRulesRequest(BaseModel):
    GroupId: StrictStr
    UserRules: list[StrictStr]
