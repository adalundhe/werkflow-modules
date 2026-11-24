from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class OpenSearchRollbackServiceSoftwareOptions(BaseModel):
    CurrentVersion: StrictStr | None = None
    NewVersion: StrictStr | None = None
    RollbackAvailable: StrictBool | None = None
    Description: StrictStr | None = None
