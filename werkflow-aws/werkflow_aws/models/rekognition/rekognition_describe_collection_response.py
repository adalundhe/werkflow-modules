from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class RekognitionDescribeCollectionResponse(BaseModel):
    FaceCount: StrictInt | None = None
    FaceModelVersion: StrictStr | None = None
    CollectionARN: StrictStr | None = None
    CreationTimestamp: datetime.datetime | StrictStr | None = None
    UserCount: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
