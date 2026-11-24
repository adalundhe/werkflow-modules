from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .f_sx_storage_virtual_machine_peer_filter import FSxStorageVirtualMachinePeerFilter


class FSxDescribeStorageVirtualMachinePeersRequest(BaseModel):
    StorageVirtualMachinePeerIds: list[StrictStr] | None = None
    Filters: list[FSxStorageVirtualMachinePeerFilter] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
