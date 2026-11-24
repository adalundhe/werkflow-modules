from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RekognitionDisassociateFacesRequest(BaseModel):
    CollectionId: StrictStr
    UserId: StrictStr
    FaceIds: list[StrictStr]
    ClientRequestToken: StrictStr | None = None
