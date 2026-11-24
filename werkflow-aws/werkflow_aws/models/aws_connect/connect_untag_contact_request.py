from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectUntagContactRequest(BaseModel):
    ContactId: StrictStr
    InstanceId: StrictStr
    TagKeys: list[StrictStr]
