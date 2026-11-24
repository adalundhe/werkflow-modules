from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FSxDeleteStorageVirtualMachinePeerRequest(BaseModel):
    StorageVirtualMachinePeerId: StrictStr
    ClientRequestToken: StrictStr | None = None
