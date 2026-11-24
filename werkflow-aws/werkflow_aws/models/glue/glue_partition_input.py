from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .glue_storage_descriptor import GlueStorageDescriptor


class GluePartitionInput(BaseModel):
    Values: list[StrictStr] | None = None
    LastAccessTime: datetime.datetime | StrictStr | None = None
    StorageDescriptor: GlueStorageDescriptor | None = None
    Parameters: dict[StrictStr, StrictStr] | None = None
    LastAnalyzedTime: datetime.datetime | StrictStr | None = None
