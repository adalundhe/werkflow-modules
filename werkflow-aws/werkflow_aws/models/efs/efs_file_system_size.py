from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class EFSFileSystemSize(BaseModel):
    Value: StrictInt | None = None
    Timestamp: datetime.datetime | StrictStr | None = None
    ValueInIA: StrictInt | None = None
    ValueInStandard: StrictInt | None = None
    ValueInArchive: StrictInt | None = None
