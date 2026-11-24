from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EMRSetVisibleToAllUsersRequest(BaseModel):
    JobFlowIds: list[StrictStr]
    VisibleToAllUsers: StrictBool
