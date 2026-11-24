from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectEmailAddressConfig(BaseModel):
    EmailAddressId: StrictStr
