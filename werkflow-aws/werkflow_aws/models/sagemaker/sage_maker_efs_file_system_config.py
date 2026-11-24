from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerEFSFileSystemConfig(BaseModel):
    FileSystemId: StrictStr | None = None
    FileSystemPath: StrictStr | None = None
