from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class DirectoryServiceUnshareTarget(BaseModel):
    Id: StrictStr
    Type: Literal['ACCOUNT']
