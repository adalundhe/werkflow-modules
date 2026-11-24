from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataSyncLocationListEntry(BaseModel):
    LocationArn: StrictStr | None = None
    LocationUri: StrictStr | None = None
