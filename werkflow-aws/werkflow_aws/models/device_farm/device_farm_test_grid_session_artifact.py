from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DeviceFarmTestGridSessionArtifact(BaseModel):
    filename: StrictStr | None = None
    type: StrictStr | None = None
    url: StrictStr | None = None
