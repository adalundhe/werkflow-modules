from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt


class FSxCreateFileSystemLustreMetadataConfiguration(BaseModel):
    Mode: Literal['AUTOMATIC', 'USER_PROVISIONED']
    Iops: StrictInt | None = None
