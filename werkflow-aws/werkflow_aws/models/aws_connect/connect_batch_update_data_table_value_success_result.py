from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_data_table_lock_version import ConnectDataTableLockVersion
from .connect_primary_value import ConnectPrimaryValue


class ConnectBatchUpdateDataTableValueSuccessResult(BaseModel):
    PrimaryValues: list[ConnectPrimaryValue] | None = None
    AttributeName: StrictStr | None = None
    LockVersion: ConnectDataTableLockVersion | None = None
