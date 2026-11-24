from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerFSxLustreFileSystemConfig(BaseModel):
    FileSystemId: StrictStr | None = None
    FileSystemPath: StrictStr | None = None
