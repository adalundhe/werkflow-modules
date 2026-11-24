from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class FSxStorageVirtualMachinePeerFilter(BaseModel):
    Name: Literal['file-system-id', 'storage-virtual-machine-id'] | None = None
    Values: list[StrictStr] | None = None
