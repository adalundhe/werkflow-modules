from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesGlobalAcceleratorForDirectory(BaseModel):
    Mode: StrictStr | None = None
    PreferredProtocol: StrictStr | None = None
