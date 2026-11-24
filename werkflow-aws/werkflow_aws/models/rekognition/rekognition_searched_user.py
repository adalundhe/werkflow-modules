from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RekognitionSearchedUser(BaseModel):
    UserId: StrictStr | None = None
