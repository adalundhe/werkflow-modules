from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .connect_data_table_lock_version import ConnectDataTableLockVersion
from .connect_primary_value import ConnectPrimaryValue


class ConnectDataTableValue(BaseModel):
    AttributeName: StrictStr
    Value: StrictStr
    PrimaryValues: list[ConnectPrimaryValue] | None = None
    LockVersion: ConnectDataTableLockVersion | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedRegion: StrictStr | None = None
