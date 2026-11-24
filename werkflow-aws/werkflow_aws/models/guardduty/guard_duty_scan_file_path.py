from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyScanFilePath(BaseModel):
    FilePath: StrictStr | None = None
    VolumeArn: StrictStr | None = None
    Hash: StrictStr | None = None
    FileName: StrictStr | None = None
