from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class RekognitionAssociateFacesRequest(BaseModel):
    CollectionId: StrictStr
    UserId: StrictStr
    FaceIds: list[StrictStr]
    UserMatchThreshold: StrictFloat | StrictInt | None = None
    ClientRequestToken: StrictStr | None = None
