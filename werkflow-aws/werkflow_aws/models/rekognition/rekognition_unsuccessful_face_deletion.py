from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RekognitionUnsuccessfulFaceDeletion(BaseModel):
    FaceId: StrictStr | None = None
    UserId: StrictStr | None = None
    Reasons: list[StrictStr] | None = None
