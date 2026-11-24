from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class RekognitionListCollectionsResponse(BaseModel):
    CollectionIds: list[StrictStr] | None = None
    NextToken: StrictStr | None = None
    FaceModelVersions: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
