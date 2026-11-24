from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class RDSDescribeDBLogFilesDetails(BaseModel):
    LogFileName: StrictStr | None = None
    LastWritten: StrictInt | None = None
    Size: StrictInt | None = None
