from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictFloat, StrictInt


class RedshiftDescribeStorageResponse(BaseModel):
    TotalBackupSizeInMegaBytes: StrictFloat | StrictInt | None = None
    TotalProvisionedStorageInMegaBytes: StrictFloat | StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
