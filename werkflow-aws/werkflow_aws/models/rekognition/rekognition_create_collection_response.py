from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class RekognitionCreateCollectionResponse(BaseModel):
    StatusCode: StrictInt | None = None
    CollectionArn: StrictStr | None = None
    FaceModelVersion: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
