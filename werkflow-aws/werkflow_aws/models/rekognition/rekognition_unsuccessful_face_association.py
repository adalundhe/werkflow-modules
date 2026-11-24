from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class RekognitionUnsuccessfulFaceAssociation(BaseModel):
    FaceId: StrictStr | None = None
    UserId: StrictStr | None = None
    Confidence: StrictFloat | StrictInt | None = None
    Reasons: list[StrictStr] | None = None
