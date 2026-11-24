from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneStorageConfig(BaseModel):
    projectS3Path: StrictStr | None = None
    kmsKeyArn: StrictStr | None = None
