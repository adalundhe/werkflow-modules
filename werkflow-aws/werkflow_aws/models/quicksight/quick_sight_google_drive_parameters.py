from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightGoogleDriveParameters(BaseModel):
    AuthType: StrictStr | None = None
