from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class DirectoryServiceEnableLDAPSRequest(BaseModel):
    DirectoryId: StrictStr
    Type: Literal['Client']
