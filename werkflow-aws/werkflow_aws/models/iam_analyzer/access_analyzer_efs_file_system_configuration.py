from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AccessAnalyzerEfsFileSystemConfiguration(BaseModel):
    fileSystemPolicy: StrictStr | None = None
