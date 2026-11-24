from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FSxDeleteStorageVirtualMachineRequest(BaseModel):
    StorageVirtualMachineId: StrictStr
    ClientRequestToken: StrictStr | None = None
