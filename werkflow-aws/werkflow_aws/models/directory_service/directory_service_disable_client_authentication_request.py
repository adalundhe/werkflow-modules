from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class DirectoryServiceDisableClientAuthenticationRequest(BaseModel):
    DirectoryId: StrictStr
    Type: Literal['SmartCard', 'SmartCardOrPassword']
