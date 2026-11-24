from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class RekognitionSearchUsersRequest(BaseModel):
    CollectionId: StrictStr
    UserId: StrictStr | None = None
    FaceId: StrictStr | None = None
    UserMatchThreshold: StrictFloat | StrictInt | None = None
    MaxUsers: StrictInt | None = None
