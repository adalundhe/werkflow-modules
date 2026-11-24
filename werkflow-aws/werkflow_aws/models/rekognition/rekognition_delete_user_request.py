from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RekognitionDeleteUserRequest(BaseModel):
    CollectionId: StrictStr
    UserId: StrictStr
    ClientRequestToken: StrictStr | None = None
