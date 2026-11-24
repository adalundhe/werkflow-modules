from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class RekognitionListFacesRequest(BaseModel):
    CollectionId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    UserId: StrictStr | None = None
    FaceIds: list[StrictStr] | None = None
