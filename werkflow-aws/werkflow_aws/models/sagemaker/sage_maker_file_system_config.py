from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerFileSystemConfig(BaseModel):
    MountPath: StrictStr | None = None
    DefaultUid: StrictInt | None = None
    DefaultGid: StrictInt | None = None
