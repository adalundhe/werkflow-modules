from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class TimestreamWriteDatabase(BaseModel):
    Arn: StrictStr | None = None
    DatabaseName: StrictStr | None = None
    TableCount: StrictInt | None = None
    KmsKeyId: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
