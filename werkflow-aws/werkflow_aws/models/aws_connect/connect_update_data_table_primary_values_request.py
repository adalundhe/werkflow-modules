from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_data_table_lock_version import ConnectDataTableLockVersion
from .connect_primary_value import ConnectPrimaryValue


class ConnectUpdateDataTablePrimaryValuesRequest(BaseModel):
    InstanceId: StrictStr
    DataTableId: StrictStr
    PrimaryValues: list[ConnectPrimaryValue]
    NewPrimaryValues: list[ConnectPrimaryValue]
    LockVersion: ConnectDataTableLockVersion
