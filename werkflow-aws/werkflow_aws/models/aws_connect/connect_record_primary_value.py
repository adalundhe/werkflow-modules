from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .connect_primary_value_response import ConnectPrimaryValueResponse


class ConnectRecordPrimaryValue(BaseModel):
    RecordId: StrictStr | None = None
    PrimaryValues: list[ConnectPrimaryValueResponse] | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedRegion: StrictStr | None = None
