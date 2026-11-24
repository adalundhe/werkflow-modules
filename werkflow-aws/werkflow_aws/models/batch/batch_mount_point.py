from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class BatchMountPoint(BaseModel):
    containerPath: StrictStr | None = None
    readOnly: StrictBool | None = None
    sourceVolume: StrictStr | None = None
