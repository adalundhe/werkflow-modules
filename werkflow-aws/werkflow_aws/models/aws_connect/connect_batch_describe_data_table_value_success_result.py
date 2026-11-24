from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .connect_data_table_lock_version import ConnectDataTableLockVersion
from .connect_primary_value_response import ConnectPrimaryValueResponse


class ConnectBatchDescribeDataTableValueSuccessResult(BaseModel):
    RecordId: StrictStr | None = None
    AttributeId: StrictStr | None = None
    PrimaryValues: list[ConnectPrimaryValueResponse] | None = None
    AttributeName: StrictStr | None = None
    Value: StrictStr | None = None
    LockVersion: ConnectDataTableLockVersion | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedRegion: StrictStr | None = None
