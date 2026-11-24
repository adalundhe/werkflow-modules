from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .athena_column import AthenaColumn


class AthenaTableMetadata(BaseModel):
    Name: StrictStr | None = None
    CreateTime: datetime.datetime | StrictStr | None = None
    LastAccessTime: datetime.datetime | StrictStr | None = None
    TableType: StrictStr | None = None
    Columns: list[AthenaColumn] | None = None
    PartitionKeys: list[AthenaColumn] | None = None
    Parameters: dict[StrictStr, StrictStr] | None = None
