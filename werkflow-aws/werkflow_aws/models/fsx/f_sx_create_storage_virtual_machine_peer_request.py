from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .f_sx_tag import FSxTag


class FSxCreateStorageVirtualMachinePeerRequest(BaseModel):
    StorageVirtualMachineId: StrictStr
    PeerSvmName: StrictStr
    Applications: list[Literal['SNAPMIRROR', 'FILE_COPY', 'LUN_COPY', 'FLEXCACHE']]
    ClientRequestToken: StrictStr | None = None
    PeerClusterName: StrictStr | None = None
    PeerSvmAlias: StrictStr | None = None
    Tags: list[FSxTag] | None = None
