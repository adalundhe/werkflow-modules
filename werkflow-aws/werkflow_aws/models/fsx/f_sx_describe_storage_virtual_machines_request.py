from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .f_sx_storage_virtual_machine_filter import FSxStorageVirtualMachineFilter


class FSxDescribeStorageVirtualMachinesRequest(BaseModel):
    StorageVirtualMachineIds: list[StrictStr] | None = None
    Filters: list[FSxStorageVirtualMachineFilter] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
