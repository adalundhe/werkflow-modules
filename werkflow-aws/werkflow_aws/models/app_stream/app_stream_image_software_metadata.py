from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppStreamImageSoftwareMetadata(BaseModel):
    nvidiaGridDriverVersion: StrictStr | None = None
