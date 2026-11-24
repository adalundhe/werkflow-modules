from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneSsoUserProfileDetails(BaseModel):
    username: StrictStr | None = None
    firstName: StrictStr | None = None
    lastName: StrictStr | None = None
