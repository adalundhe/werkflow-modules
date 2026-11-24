from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class FSxUpdateStorageVirtualMachinePeerRequest(BaseModel):
    StorageVirtualMachinePeerId: StrictStr
    ClientRequestToken: StrictStr | None = None
    Applications: list[Literal['SNAPMIRROR', 'FILE_COPY', 'LUN_COPY', 'FLEXCACHE']] | None = None
    PeerSvmAlias: StrictStr | None = None
    State: Literal['PEERED', 'REJECTED', 'SUSPENDED'] | None = None
