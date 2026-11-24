from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataSyncUpdateLocationFsxLustreRequest(BaseModel):
    LocationArn: StrictStr
    Subdirectory: StrictStr | None = None
