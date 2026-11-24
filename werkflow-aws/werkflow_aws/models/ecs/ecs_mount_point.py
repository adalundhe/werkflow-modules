from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class ECSMountPoint(BaseModel):
    sourceVolume: StrictStr | None = None
    containerPath: StrictStr | None = None
    readOnly: StrictBool | None = None
