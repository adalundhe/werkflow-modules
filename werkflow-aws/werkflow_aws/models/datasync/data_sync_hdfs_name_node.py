from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DataSyncHdfsNameNode(BaseModel):
    Hostname: StrictStr | None = None
    Port: StrictInt | None = None
