from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class DataSyncUpdateLocationEfsRequest(BaseModel):
    LocationArn: StrictStr
    Subdirectory: StrictStr | None = None
    AccessPointArn: StrictStr | None = None
    FileSystemAccessRoleArn: StrictStr | None = None
    InTransitEncryption: Literal['NONE', 'TLS1_2'] | None = None
