from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class RekognitionListUsersRequest(BaseModel):
    CollectionId: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
