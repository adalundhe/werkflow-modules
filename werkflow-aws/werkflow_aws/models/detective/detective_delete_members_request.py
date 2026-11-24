from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DetectiveDeleteMembersRequest(BaseModel):
    GraphArn: StrictStr
    AccountIds: list[StrictStr]
