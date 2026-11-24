from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class CognitoSyncRecordPatch(BaseModel):
    Op: Literal['replace', 'remove']
    Key: StrictStr
    SyncCount: StrictInt
    Value: StrictStr | None = None
    DeviceLastModifiedDate: datetime.datetime | StrictStr | None = None
