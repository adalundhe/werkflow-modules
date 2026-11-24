from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .connect_data_table_lock_version import ConnectDataTableLockVersion


class ConnectDataTable(BaseModel):
    Name: StrictStr | None = None
    Id: StrictStr | None = None
    Arn: StrictStr | None = None
    TimeZone: StrictStr | None = None
    Description: StrictStr | None = None
    ValueLockLevel: StrictStr | None = None
    LockVersion: ConnectDataTableLockVersion | None = None
    Version: StrictStr | None = None
    VersionDescription: StrictStr | None = None
    Status: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedRegion: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
