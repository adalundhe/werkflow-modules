from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt


class FSxUpdateFileSystemLustreMetadataConfiguration(BaseModel):
    Iops: StrictInt | None = None
    Mode: Literal['AUTOMATIC', 'USER_PROVISIONED'] | None = None
