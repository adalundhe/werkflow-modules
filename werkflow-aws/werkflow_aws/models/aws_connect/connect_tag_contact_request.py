from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectTagContactRequest(BaseModel):
    ContactId: StrictStr
    InstanceId: StrictStr
    Tags: dict[StrictStr, StrictStr]
