from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DetectiveGetMembersRequest(BaseModel):
    GraphArn: StrictStr
    AccountIds: list[StrictStr]
