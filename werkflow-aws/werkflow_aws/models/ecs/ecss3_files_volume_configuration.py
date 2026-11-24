from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ECSS3FilesVolumeConfiguration(BaseModel):
    fileSystemArn: StrictStr | None = None
    rootDirectory: StrictStr | None = None
    transitEncryptionPort: StrictInt | None = None
    accessPointArn: StrictStr | None = None
