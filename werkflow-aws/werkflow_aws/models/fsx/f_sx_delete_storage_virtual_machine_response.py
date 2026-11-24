from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class FSxDeleteStorageVirtualMachineResponse(BaseModel):
    StorageVirtualMachineId: StrictStr | None = None
    Lifecycle: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
