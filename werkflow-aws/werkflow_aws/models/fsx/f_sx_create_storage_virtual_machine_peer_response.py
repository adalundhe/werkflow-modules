from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .f_sx_storage_virtual_machine_peer import FSxStorageVirtualMachinePeer


class FSxCreateStorageVirtualMachinePeerResponse(BaseModel):
    StorageVirtualMachinePeer: FSxStorageVirtualMachinePeer | None = None
    ResponseMetadata: dict[str, Any] | None = None
