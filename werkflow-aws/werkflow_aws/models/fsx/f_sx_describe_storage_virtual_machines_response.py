from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .f_sx_storage_virtual_machine import FSxStorageVirtualMachine


class FSxDescribeStorageVirtualMachinesResponse(BaseModel):
    StorageVirtualMachines: list[FSxStorageVirtualMachine] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
