from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerEFSFileSystem(BaseModel):
    FileSystemId: StrictStr | None = None
