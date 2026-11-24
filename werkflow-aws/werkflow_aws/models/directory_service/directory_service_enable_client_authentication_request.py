from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class DirectoryServiceEnableClientAuthenticationRequest(BaseModel):
    DirectoryId: StrictStr
    Type: Literal['SmartCard', 'SmartCardOrPassword']
