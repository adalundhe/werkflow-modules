from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MQDeleteUserRequest(BaseModel):
    BrokerId: StrictStr
    Username: StrictStr
