from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class FSxFileSystemLustreMetadataConfiguration(BaseModel):
    Iops: StrictInt | None = None
    Mode: StrictStr | None = None
