from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .detective_account import DetectiveAccount


class DetectiveCreateMembersRequest(BaseModel):
    GraphArn: StrictStr
    Accounts: list[DetectiveAccount]
    Message: StrictStr | None = None
    DisableEmailNotification: StrictBool | None = None
