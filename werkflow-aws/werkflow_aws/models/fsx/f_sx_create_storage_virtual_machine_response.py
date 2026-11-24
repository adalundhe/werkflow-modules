from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .f_sx_storage_virtual_machine import FSxStorageVirtualMachine


class FSxCreateStorageVirtualMachineResponse(BaseModel):
    StorageVirtualMachine: FSxStorageVirtualMachine | None = None
    ResponseMetadata: dict[str, Any] | None = None
