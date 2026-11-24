from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_user_proficiency_disassociate import ConnectUserProficiencyDisassociate


class ConnectDisassociateUserProficienciesRequest(BaseModel):
    InstanceId: StrictStr
    UserId: StrictStr
    UserProficiencies: list[ConnectUserProficiencyDisassociate]
