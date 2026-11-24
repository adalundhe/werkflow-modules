from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerFSxLustreFileSystem(BaseModel):
    FileSystemId: StrictStr | None = None
