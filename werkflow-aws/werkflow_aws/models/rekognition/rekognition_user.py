from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RekognitionUser(BaseModel):
    UserId: StrictStr | None = None
    UserStatus: StrictStr | None = None
