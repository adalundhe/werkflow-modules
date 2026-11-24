from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class WorkSpacesUpdateResult(BaseModel):
    UpdateAvailable: StrictBool | None = None
    Description: StrictStr | None = None
