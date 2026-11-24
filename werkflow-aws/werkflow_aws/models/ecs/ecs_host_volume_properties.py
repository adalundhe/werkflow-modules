from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSHostVolumeProperties(BaseModel):
    sourcePath: StrictStr | None = None
