from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class DynamoDBListBackupsRequest(BaseModel):
    TableName: StrictStr | None = None
    Limit: StrictInt | None = None
    TimeRangeLowerBound: datetime.datetime | StrictStr | None = None
    TimeRangeUpperBound: datetime.datetime | StrictStr | None = None
    ExclusiveStartBackupArn: StrictStr | None = None
    BackupType: Literal['USER', 'SYSTEM', 'AWS_BACKUP', 'ALL'] | None = None
