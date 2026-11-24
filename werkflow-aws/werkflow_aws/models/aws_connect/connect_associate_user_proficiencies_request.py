from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_user_proficiency import ConnectUserProficiency


class ConnectAssociateUserProficienciesRequest(BaseModel):
    InstanceId: StrictStr
    UserId: StrictStr
    UserProficiencies: list[ConnectUserProficiency]
