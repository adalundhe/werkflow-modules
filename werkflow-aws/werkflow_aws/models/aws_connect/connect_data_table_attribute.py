from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .connect_data_table_lock_version import ConnectDataTableLockVersion
from .connect_validation import ConnectValidation


class ConnectDataTableAttribute(BaseModel):
    AttributeId: StrictStr | None = None
    Name: StrictStr | None = None
    ValueType: StrictStr | None = None
    Description: StrictStr | None = None
    DataTableId: StrictStr | None = None
    DataTableArn: StrictStr | None = None
    Primary: StrictBool | None = None
    Version: StrictStr | None = None
    LockVersion: ConnectDataTableLockVersion | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedRegion: StrictStr | None = None
    Validation: ConnectValidation | None = None
